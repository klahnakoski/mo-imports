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


class TestExport(TestCase):
    def test_wait_time(self):
        self.assertEqual(mo_imports.WAIT_FOR_EXPORT, 10)
