#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_dupes
----------------------------------

Tests for `dupes` module.
"""


import mock
import unittest

from dupes import Dupes


class TestDupes(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_get_files(self):

        d = Dupes()
        with mock.patch('dupes.os.listdir') as mock_listdir:
            with mock.patch('dupes.os.path.isfile') as mock_isfile:
                mock_listdir.return_value = ['a', 'b', 'c']
                mock_isfile.return_value = True
                d.get_files()

        self.assertEqual(d.files, ['a', 'b', 'c'])

if __name__ == '__main__':
    unittest.main()
