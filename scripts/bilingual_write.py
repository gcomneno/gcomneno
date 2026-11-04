"""Recoverable replacement of two rendered, validated profile READMEs.

Callers must snapshot before rendering and validate both outputs before calling
write_bilingual. Originals and replacements are staged beside each destination.
This is NOT a crash-atomic two-file transaction: interruption or power loss can
leave mixed versions and recovery files. There is no automatic crash recovery.

Identity, bytes and permissions are checked before replacement and rollback.
These optimistic checks cannot close the check-to-os.replace race or prevent an
edit after the final check. Writers must be externally serialized for that
guarantee; no portable two-path compare-and-swap is provided here.
"""

from __future__ import annotations

import os
import stat
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path


class BilingualWriteError(RuntimeError):
    pass


class RecoveryRequiredError(BilingualWriteError):
    def __init__(self, backups: dict[Path, Path]) -> None:
        self.backups = backups.copy()
        recovery = "; ".join(
            f"{destination} <- {backup}"
            for destination, backup in backups.items()
        )
        super().__init__(
            f"Recovery required: rollback incomplete. Original backups: {recovery}"
        )


@dataclass(frozen=True)
class FileSnapshot:
    data: bytes
    metadata: os.stat_result

    @property
    def text(self) -> str:
        return self.data.decode("utf-8")


def _identity(metadata: os.stat_result) -> tuple[int, ...]:
    # Rename can change ctime, so it is deliberately excluded.
    return (
        metadata.st_dev,
        metadata.st_ino,
        metadata.st_mode,
        metadata.st_size,
        metadata.st_mtime_ns,
    )


def read_snapshot(path: Path) -> FileSnapshot:
    before = path.lstat()
    if not stat.S_ISREG(before.st_mode):
        raise BilingualWriteError(f"Expected a regular README file: {path}")
    with path.open("rb") as stream:
        opened = os.fstat(stream.fileno())
        data = stream.read()
        after = os.fstat(stream.fileno())
    if not (
        _identity(before) == _identity(opened)
        == _identity(after) == _identity(path.lstat())
    ):
        raise BilingualWriteError(f"Concurrent change detected: {path}")
    return FileSnapshot(data, after)


def _check_unchanged(path: Path, expected: FileSnapshot) -> None:
    current = read_snapshot(path)
    if (
        _identity(current.metadata) != _identity(expected.metadata)
        or current.data != expected.data
    ):
        raise BilingualWriteError(f"Concurrent change detected: {path}")


def _stage(path: Path, data: bytes, mode: int, suffix: str) -> Path:
    staged = None
    try:
        with tempfile.NamedTemporaryFile(
            prefix=f".{path.name}.", suffix=suffix, dir=path.parent, delete=False
        ) as stream:
            staged = Path(stream.name)
            stream.write(data)
            stream.flush()
            os.fchmod(stream.fileno(), mode)
            os.fsync(stream.fileno())
    except BaseException:
        if staged is not None:
            staged.unlink(missing_ok=True)
        raise
    return staged


def write_bilingual(
    originals: dict[Path, FileSnapshot], outputs: dict[Path, str]
) -> list[Path]:
    """Return changed paths, or raise; retain original backups if rollback fails."""
    if (
        len(originals) != 2
        or originals.keys() != outputs.keys()
        or len({path.resolve() for path in originals}) != 2
    ):
        raise BilingualWriteError("Expected two distinct README paths and outputs.")

    # Encode every output before staging, including an otherwise unchanged file.
    encoded = {path: content.encode("utf-8") for path, content in outputs.items()}
    changed = [path for path in originals if encoded[path] != originals[path].data]
    temporary: list[Path] = []
    backups: dict[Path, Path] = {}
    replacements: dict[Path, Path] = {}
    installed: dict[Path, FileSnapshot] = {}
    replaced: list[Path] = []
    recovery_required = False
    try:
        for path in changed:
            original = originals[path]
            mode = stat.S_IMODE(original.metadata.st_mode)
            backups[path] = _stage(path, original.data, mode, ".original")
            temporary.append(backups[path])
            replacements[path] = _stage(path, encoded[path], mode, ".replacement")
            temporary.append(replacements[path])
            installed[path] = read_snapshot(replacements[path])

        # Include unchanged counterparts in conflict detection.
        for path, original in originals.items():
            _check_unchanged(path, original)
        for path in changed:
            _check_unchanged(path, originals[path])
            os.replace(replacements[path], path)
            replaced.append(path)
        for path, original in originals.items():
            _check_unchanged(path, installed.get(path, original))
    except BaseException as exc:
        for path in reversed(replaced):
            try:
                # Do not undo a third-party edit made after our replacement.
                _check_unchanged(path, installed[path])
                original = originals[path]
                restore = _stage(
                    path, original.data, stat.S_IMODE(original.metadata.st_mode),
                    ".restore",
                )
                temporary.append(restore)
                _check_unchanged(path, installed[path])
                os.replace(restore, path)
            except BaseException:
                recovery_required = True
        if recovery_required:
            raise RecoveryRequiredError(backups) from exc
        raise BilingualWriteError(
            f"Bilingual write failed; completed replacements rolled back: {exc}"
        ) from exc
    finally:
        cleanup_errors = []
        for staged in temporary:
            if recovery_required and staged in backups.values():
                continue
            try:
                staged.unlink(missing_ok=True)
            except OSError as exc:
                cleanup_errors.append(f"{staged}: {exc}")
        if cleanup_errors:
            message = "Temporary file cleanup failed: " + "; ".join(cleanup_errors)
            # Cleanup must never mask the rollback/recovery diagnostic.
            if sys.exc_info()[0] is None:
                raise BilingualWriteError(f"README replacements completed. {message}")
            print(message, file=sys.stderr)
    return changed
