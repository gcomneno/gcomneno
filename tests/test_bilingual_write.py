from __future__ import annotations

import os
import stat
import io
import unittest
from contextlib import redirect_stderr
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch

from scripts import bilingual_write as writer


class BilingualWriteTests(unittest.TestCase):
    def setUp(self) -> None:
        self.directory = TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        # Different parents ensure each stage is beside its own destination.
        self.en = self.root / "en" / "README.md"
        self.it = self.root / "it" / "README.it.md"
        for path, data, mode in (
            (self.en, b"Original English\r\n", 0o640),
            (self.it, "Originale italiano è\r\n".encode("utf-8"), 0o604),
        ):
            path.parent.mkdir()
            path.write_bytes(data)
            path.chmod(mode)
        self.originals = {
            path: writer.read_snapshot(path) for path in (self.en, self.it)
        }
        self.outputs = {self.en: "Updated English\n", self.it: "Italiano aggiornato\n"}
        self.real_replace = os.replace

    def assert_originals(self) -> None:
        for path, snapshot in self.originals.items():
            self.assertEqual(path.read_bytes(), snapshot.data)
            self.assertEqual(
                stat.S_IMODE(path.stat().st_mode),
                stat.S_IMODE(snapshot.metadata.st_mode),
            )

    def assert_no_temporary_files(self) -> None:
        self.assertEqual(set(self.root.rglob(".*")), set())

    def assert_backups(self, error: writer.RecoveryRequiredError) -> None:
        self.assertEqual(error.backups.keys(), self.originals.keys())
        for path, backup in error.backups.items():
            self.assertEqual(backup.parent, path.parent)
            self.assertEqual(backup.read_bytes(), self.originals[path].data)
            self.assertEqual(
                stat.S_IMODE(backup.stat().st_mode),
                stat.S_IMODE(self.originals[path].metadata.st_mode),
            )
            self.assertIn(str(backup), str(error))
        self.assertEqual(set(self.root.rglob(".*")), set(error.backups.values()))

    def test_success_preserves_permissions_and_stages_beside_each_destination(self) -> None:
        def replace(source: Path, destination: Path) -> None:
            self.assertEqual(source.parent, destination.parent)
            # All backups and replacements exist before the first mutation.
            if destination == self.en:
                self.assertEqual(len(list(self.root.rglob(".*"))), 4)
                self.assert_originals()
            self.real_replace(source, destination)

        with patch.object(writer.os, "replace", side_effect=replace):
            self.assertEqual(
                writer.write_bilingual(self.originals, self.outputs),
                [self.en, self.it],
            )
        for path, content in self.outputs.items():
            self.assertEqual(path.read_bytes(), content.encode("utf-8"))
            self.assertEqual(
                stat.S_IMODE(path.stat().st_mode),
                stat.S_IMODE(self.originals[path].metadata.st_mode),
            )
        self.assert_no_temporary_files()

    def test_staging_failure_leaves_originals_untouched(self) -> None:
        create = writer.tempfile.NamedTemporaryFile
        calls = 0

        def fail_last_stage(*args, **kwargs):
            nonlocal calls
            calls += 1
            if calls == 4:
                raise OSError("staging failed")
            return create(*args, **kwargs)

        with (
            patch.object(writer.tempfile, "NamedTemporaryFile", side_effect=fail_last_stage),
            patch.object(writer.os, "replace") as replace,
        ):
            with self.assertRaisesRegex(writer.BilingualWriteError, "staging failed"):
                writer.write_bilingual(self.originals, self.outputs)
            replace.assert_not_called()
        self.assert_originals()
        for path, original in self.originals.items():
            self.assertEqual(path.stat().st_ino, original.metadata.st_ino)
        self.assert_no_temporary_files()

    def test_stage_write_failure_removes_incomplete_stage(self) -> None:
        with patch.object(writer.os, "fsync", side_effect=OSError("flush failed")):
            with self.assertRaisesRegex(writer.BilingualWriteError, "flush failed"):
                writer.write_bilingual(self.originals, self.outputs)
        self.assert_originals()
        self.assert_no_temporary_files()

    def test_second_replacement_failure_rolls_back_original_bytes_and_permissions(self) -> None:
        def replace(source: Path, destination: Path) -> None:
            if destination == self.it:
                raise OSError("second replacement failed")
            self.real_replace(source, destination)

        with patch.object(writer.os, "replace", side_effect=replace) as replace_mock:
            with self.assertRaisesRegex(writer.BilingualWriteError, "rolled back"):
                writer.write_bilingual(self.originals, self.outputs)
            self.assertEqual(replace_mock.call_count, 3)
        self.assert_originals()
        self.assert_no_temporary_files()

    def test_rollback_failure_keeps_original_backups_and_reports_recovery(self) -> None:
        for fail_restore_stage in (False, True):
            with self.subTest(fail_restore_stage=fail_restore_stage):
                originals = {path: writer.read_snapshot(path) for path in self.originals}
                self.originals = originals
                stage = writer._stage

                def replace(source: Path, destination: Path) -> None:
                    if destination == self.it or source.suffix == ".restore":
                        raise OSError("replacement failed")
                    self.real_replace(source, destination)

                def stage_or_fail(path, data, mode, suffix):
                    if fail_restore_stage and suffix == ".restore":
                        raise OSError("rollback staging failed")
                    return stage(path, data, mode, suffix)

                with (
                    patch.object(writer.os, "replace", side_effect=replace),
                    patch.object(writer, "_stage", side_effect=stage_or_fail),
                ):
                    with self.assertRaisesRegex(
                        writer.RecoveryRequiredError, "Recovery required"
                    ) as raised:
                        writer.write_bilingual(self.originals, self.outputs)
                self.assertEqual(self.en.read_bytes(), self.outputs[self.en].encode())
                self.assertEqual(self.it.read_bytes(), originals[self.it].data)
                self.assert_backups(raised.exception)
                # Exercise manual recovery before the next subtest.
                for path, backup in raised.exception.backups.items():
                    self.real_replace(backup, path)

    def test_edit_after_snapshot_is_detected_without_overwrite(self) -> None:
        self.it.write_bytes(b"Third-party edit\n")
        with patch.object(writer.os, "replace") as replace:
            with self.assertRaisesRegex(writer.BilingualWriteError, "Concurrent change"):
                writer.write_bilingual(self.originals, self.outputs)
            replace.assert_not_called()
        self.assertEqual(self.it.read_bytes(), b"Third-party edit\n")
        self.assertEqual(self.en.read_bytes(), self.originals[self.en].data)
        self.assert_no_temporary_files()

    def test_edit_between_replacements_is_preserved_and_first_file_rolled_back(self) -> None:
        def replace(source: Path, destination: Path) -> None:
            self.real_replace(source, destination)
            if destination == self.en and source.suffix == ".replacement":
                self.it.write_bytes(b"Third-party edit\n")

        with patch.object(writer.os, "replace", side_effect=replace):
            with self.assertRaisesRegex(writer.BilingualWriteError, "Concurrent change"):
                writer.write_bilingual(self.originals, self.outputs)
        self.assertEqual(self.en.read_bytes(), self.originals[self.en].data)
        self.assertEqual(self.it.read_bytes(), b"Third-party edit\n")
        self.assert_no_temporary_files()

    def test_rollback_does_not_overwrite_concurrent_edit(self) -> None:
        def replace(source: Path, destination: Path) -> None:
            if destination == self.it:
                self.en.write_bytes(b"Third-party edit\n")
                raise OSError("second replacement failed")
            self.real_replace(source, destination)

        with patch.object(writer.os, "replace", side_effect=replace):
            with self.assertRaises(writer.RecoveryRequiredError) as raised:
                writer.write_bilingual(self.originals, self.outputs)
        self.assertEqual(self.en.read_bytes(), b"Third-party edit\n")
        self.assert_backups(raised.exception)

    def test_unchanged_file_is_checked_but_not_replaced(self) -> None:
        self.outputs[self.it] = self.originals[self.it].text
        self.assertEqual(
            writer.write_bilingual(self.originals, self.outputs), [self.en]
        )
        self.assertEqual(self.it.stat().st_ino, self.originals[self.it].metadata.st_ino)
        self.assert_no_temporary_files()

    def test_no_changes_does_not_stage_or_replace(self) -> None:
        outputs = {path: snapshot.text for path, snapshot in self.originals.items()}
        with patch.object(writer, "_stage") as stage:
            self.assertEqual(writer.write_bilingual(self.originals, outputs), [])
            stage.assert_not_called()
        self.assert_originals()
        self.assert_no_temporary_files()

    def test_both_outputs_encoded_before_any_staging(self) -> None:
        self.outputs[self.it] = "invalid UTF-8 surrogate: \ud800"
        with patch.object(writer, "_stage") as stage:
            with self.assertRaises(UnicodeEncodeError):
                writer.write_bilingual(self.originals, self.outputs)
            stage.assert_not_called()
        self.assert_originals()

    def test_cleanup_failure_is_not_reported_as_success(self) -> None:
        unlink = Path.unlink

        def fail_backup_cleanup(path, *args, **kwargs):
            if path.suffix == ".original":
                raise OSError("cleanup failed")
            return unlink(path, *args, **kwargs)

        with patch.object(Path, "unlink", fail_backup_cleanup):
            with self.assertRaisesRegex(
                writer.BilingualWriteError,
                "README replacements completed.*cleanup failed",
            ):
                writer.write_bilingual(self.originals, self.outputs)
        for path, content in self.outputs.items():
            self.assertEqual(path.read_bytes(), content.encode())

    def test_cleanup_failure_cannot_mask_recovery_diagnostic(self) -> None:
        unlink = Path.unlink

        def replace(source, destination):
            if destination == self.it or source.suffix == ".restore":
                raise OSError("replacement failed")
            self.real_replace(source, destination)

        def fail_restore_cleanup(path, *args, **kwargs):
            if path.suffix == ".restore":
                raise OSError("cleanup failed")
            return unlink(path, *args, **kwargs)

        stderr = io.StringIO()
        with (
            patch.object(writer.os, "replace", side_effect=replace),
            patch.object(Path, "unlink", fail_restore_cleanup),
            redirect_stderr(stderr),
        ):
            with self.assertRaisesRegex(
                writer.RecoveryRequiredError, "Recovery required"
            ) as raised:
                writer.write_bilingual(self.originals, self.outputs)
        self.assertIn("cleanup failed", stderr.getvalue())
        for path, backup in raised.exception.backups.items():
            self.assertEqual(backup.read_bytes(), self.originals[path].data)


if __name__ == "__main__":
    unittest.main()
