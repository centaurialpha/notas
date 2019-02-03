import unittest
import shlex

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
            'open some_note',
            'rm note_to_remove'
        ]
        for line in cmd:
            cmdline = shlex.split(line)
            self._parser.parse_args(cmdline)

    def test_parser_args_invalid(self):
        cmd = [
            'new file file',
            'ls file',
            'rm',
            'open note note'
        ]
        for line in cmd:
            cmdline = shlex.split(line)
            with self.assertRaises(SystemExit) as e:
                self._parser.parse_args(cmdline)
            self.assertEqual(2, e.exception.code)