import mo_imports

from mo_imports import delay_import

Log = delay_import("mo_logs.Log")


def delay_get(self):
    self.assertIsInstance(Log, mo_imports.DelayedImport)
    value = Log.trace
    self.assertNotIsInstance(Log, mo_imports.DelayedImport)
