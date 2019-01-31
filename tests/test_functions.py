# -*- coding: utf-8 -*-
#
# This file is part of Notas(http://ninja-ide.org).
#
# Notasis free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# any later version.
#
# Notasis distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Notas; If not, see <http://www.gnu.org/licenses/>.


import unittest
import tempfile
import shutil
import os
import shlex

from notas import functions
from notas import cli


class CLITestCase(unittest.TestCase):

    def setUp(self):
        self._parser = cli.cliparse()

    def test_parser_help(self):
        with self.assertRaises(SystemExit):
            self._parser.parse_args(['--help'])

    def test_parser_args_valid(self):
        cmd = [
            'new file',
            'ls',
            'rm file',
        ]
        for line in cmd:
            cmdline = shlex.split(line)
            self._parser.parse_args(cmdline)

    def test_parser_args_invalid(self):
        cmd = [
            'new file file',
            'ls file',
            'rm'
        ]
        for line in cmd:
            cmdline = shlex.split(line)
            with self.assertRaises(SystemExit) as e:
                self._parser.parse_args(cmdline)
            self.assertEqual(2, e.exception.code)


class FunctionsTestCase(unittest.TestCase):

    def setUp(self):
        self._dir = tempfile.mkdtemp()
        functions.NOTES_PATH = self._dir
        for f in ('f1', 'f2', 'f3'):
            with open(os.path.join(self._dir, f), 'w') as fp:
                fp.write('some content {}'.format(f))

    def tearDown(self):
        shutil.rmtree(self._dir)

    def test_get_base_name(self):
        for f in ('f1', 'f2', 'f3'):
            file_path = os.path.join(self._dir, f)
            self.assertEqual(functions.get_basename(file_path), f)


if __name__ == '__main__':
    unittest.main()
