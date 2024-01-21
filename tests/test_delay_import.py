# encoding: utf-8
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Contact: Kyle Lahnakoski (kyle@lahnakoski.com)
#
from unittest import TestCase

from mo_imports import delay_import

make_value = delay_import("tests.delayed_value1.make_value")


class TestDelayImport(TestCase):

    def test_delay(self):
        a = make_value
        self.assertEqual(make_value(), "hello world")
        self.assertEqual(a(), "hello world")
