import mo_imports

from mo_imports import delay_import

threading = delay_import("threading")


def delay_simple_get(self):
    self.assertIsInstance(threading, mo_imports.DelayedImport)
    value = threading._trace_hook
    self.assertNotIsInstance(threading, mo_imports.DelayedImport)
