import os
import unittest
import tempfile
import shutil
from unittest import mock

from notas import utils
import notas


class UtilsTestCase(unittest.TestCase):

    def setUp(self):
        self._dir = tempfile.mkdtemp()
        notas.NOTES_PATH = self._dir

    def tearDown(self):
        shutil.rmtree(self._dir)

    def test_get_basename(self):
        notes = (
            'pat/to/note/note_1',
            'pat/to/note/note_2',
            'pat/to/note/note_3'
        )
        expected = (
            'note_1',
            'note_2',
            'note_3'
        )
        for note, bname in zip(notes, expected):
            self.assertEqual(utils.get_basename(note), bname)

    def _create_note(self, name):
        note_path = os.path.join(self._dir, name)
        with open(note_path, 'w') as fp:
            fp.write('Some content {}'.format(name))
        return note_path

    def test_get_all_notes(self):
        fname_notes = ('n1', 'n2', 'n3', 'n4')
        notes = [self._create_note(n) for n in fname_notes]
        self.assertEqual(len(utils.get_all_notes(self._dir)), 4)
        self.assertEqual(sorted(utils.get_all_notes(self._dir)), notes)

    def test_get_note_by_number(self):
        fname_notes = ('n1', 'n2', 'n3', 'n4')
        notes = [self._create_note(n) for n in fname_notes]
        with mock.patch('notas.utils.get_all_notes', return_value=notes):
            user_input = [2, 0]
            for i in user_input:
                note = utils.get_note_by_number(i)
                self.assertEqual(note, os.path.join(self._dir, notes[i]))

    def test_get_note_by_number_raise(self):
        fname_notes = ('n1', 'n2', 'n3', 'n4')
        notes = [self._create_note(n) for n in fname_notes]
        with mock.patch('notas.utils.get_all_notes', return_value=notes):
            user_input = 8
            with self.assertRaises(utils.NoteNotFoundError):
                utils.get_note_by_number(user_input)

    def test_get_note_by_name(self):
        fname_notes = ('n1', 'n2', 'n3', 'n4')
        notes = [self._create_note(n) for n in fname_notes]
        with mock.patch('notas.utils.get_all_notes', return_value=notes):
            user_input = ['n3', 'n1']
            for i in user_input:
                note = utils.get_note_by_name(i)
                self.assertEqual(note, os.path.join(self._dir, i))

    def test_get_note_by_name_raises(self):
        fname_notes = ('n1', 'n2', 'n3', 'n4')
        notes = [self._create_note(n) for n in fname_notes]
        with mock.patch('notas.utils.get_all_notes', return_value=notes):
            user_input = 'fooooooo'
            with self.assertRaises(utils.NoteNotFoundError):
                utils.get_note_by_name(user_input)

    def test_get_note(self):
        with mock.patch('notas.utils.get_note_by_number') as mocked:
            utils.get_note(1)
            self.assertTrue(mocked.called)
        with mock.patch('notas.utils.get_note_by_name') as mocked:
            utils.get_note('')
            self.assertTrue(mocked.called)

    def test_note_exists(self):
        with mock.patch('notas.utils.NOTES_PATH', self._dir):
            tmp_note = tempfile.mkstemp(dir=self._dir)[1]
            base_name = os.path.basename(tmp_note)
            self.assertTrue(utils.note_exists(base_name))

    def test_get_note_path(self):
        with mock.patch('notas.utils.NOTES_PATH', self._dir):
            note = 'test_note_1'
            self.assertEqual(utils.get_note_path(note), os.path.join(self._dir, note))

    def test_get_editor_custom(self):
        with mock.patch('notas.utils.shutil.which', return_value='ninja-ide'):
            self.assertEqual(utils.get_editor('ninja-ide'), 'ninja-ide')

    def test_get_editor_custom_raises(self):
        with mock.patch('notas.utils.shutil.which', return_value=None):
            with self.assertRaises(utils.NotEditorFoundError):
                utils.get_editor('algun_editor')

    def test_get_editor_environ_ok(self):
        with mock.patch('notas.utils.os.environ', {'EDITOR': 'super_editor'}):
            self.assertEqual(utils.get_editor(), 'super_editor')

    def test_get_editor_not_environ_default_ok(self):
        with mock.patch('notas.utils.os.environ', {'EDITOR': None}):
            with mock.patch('notas.utils.shutil.which', return_value='/usr/bin/editor'):
                self.assertEqual(utils.get_editor(), '/usr/bin/editor')

    def test_get_editor_not_environ_default_raises(self):
        with mock.patch('notas.utils.os.environ', {'EDITOR': None}):
            with mock.patch('notas.utils.shutil.which', return_value=None):
                with self.assertRaises(utils.NotEditorFoundError):
                    utils.get_editor()

    def test_rm_note(self):
        notes_to_remove = ('note_1', 'note_2', 'note_1222')
        notes_to_remove = [self._create_note(n) for n in notes_to_remove]
        with mock.patch('notas.utils.get_all_notes', return_value=notes_to_remove):
            utils.remove_note('note_2')
            utils.remove_note('note_1')
            notes = os.listdir(self._dir)
            self.assertEqual(len(notes), 1)
            self.assertEqual(notes, ['note_1222'])


if __name__ == '__main__':
    unittest.main()
