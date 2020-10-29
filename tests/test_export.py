from unittest import TestCase

import mo_imports
from mo_imports import delay_import

Log = delay_import("mo_logs.Log")


class TestExport(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.old, mo_imports.WAIT_FOR_EXPORT = mo_imports.WAIT_FOR_EXPORT, 1

    @classmethod
    def tearDownClass(cls):
        mo_imports.WAIT_FOR_EXPORT = cls.old

    def test_delay(self):
        try:
            Log.error("expected to throw")
        except Exception as cause:
            if "expected to throw" not in cause:
                raise Exception("not expected")

    def test_modname_name1(self):
        from tests.modname_name1.foos import foo
        _ = foo

    def test_modname_name_value1(self):
        from tests.modname_name_value1.foos import foo
        _ = foo

    def test_modname_value1(self):
        from tests.modname_value1.foos import foo
        _ = foo

    def test_module_name1(self):
        from tests.module_name1.foos import foo
        _ = foo

    def test_module_name_value1(self):
        from tests.module_name_value1.foos import foo
        _ = foo

    def test_module_value1(self):
        from tests.module_value1.foos import foo
        _ = foo

    def test_module_value2(self):
        from tests.module_value2.foos import foo
        _ = foo

    def test_missing_export(self):
        pass

    def test_missing_expect(self):
        pass

    def test_delay_import(self):
        pass