# encoding: utf-8
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Contact: Kyle Lahnakoski (kyle@lahnakoski.com)
#
from unittest import TestCase

import mo_imports
from mo_imports import delay_import

Log = delay_import("mo_logs.Log")
threading = delay_import("threading")

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

    def test_delay_set(self):
        from tests.module_set_attr import delay_set
        delay_set(self)

    def test_delay_get(self):
        from tests.module_get_attr import delay_get
        delay_get(self)

    def test_delay_simple_get(self):
        from tests.module_get_simple_attr import delay_simple_get
        delay_simple_get(self)

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
