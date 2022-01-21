import mo_imports

from mo_imports import delay_import

Log = delay_import("mo_logs.Log")


def delay_set(self):
    self.assertIsInstance(Log, mo_imports.DelayedImport)
    Log.trace = True
    self.assertNotIsInstance(Log, mo_imports.DelayedImport)
    self.assertEqual(Log.trace, True)
