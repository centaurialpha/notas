# -*- coding: utf-8 -*-
#
# Copyright 2019 - Gabriel Acosta <acostadariogabriel@gmail.com>
#
# This file is part of Notas.
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

import os
import shutil

# Here the notes will be stored
NOTES_PATH = os.path.join(os.path.expanduser('~'), '.notas')
# Create path if not exists
if not os.path.exists(NOTES_PATH):
    os.makedirs(NOTES_PATH)


class NotEditorFoundError(Exception):
    pass


class NoteNotFoundError(Exception):
    pass


def remove_note(name: str):
    try:
        os.remove(get_note_by_name(name))
    except FileNotFoundError:
        raise NoteNotFoundError("Note not found!")


def get_editor(custom_editor=None):
    """Try to get default editor in system. Raises if not"""
    editor = os.environ.get('EDITOR', None)
    if editor is None:
        if custom_editor is not None:
            editor = shutil.which(custom_editor)
        else:
            editor = shutil.which('editor')
        if editor is None:
            raise NotEditorFoundError("Editor not exists :(")
    return editor


def get_note_path(note_name: str) -> str:
    return os.path.join(NOTES_PATH, note_name)


def get_basename(file_path: str) -> str:
    """Returns the basename of `file_path`"""
    return os.path.basename(file_path)


def note_exists(note_name: str) -> bool:
    """Returns True if `note_name` exists, otherwise False"""
    return os.path.exists(os.path.join(NOTES_PATH, note_name))


def get_note_by_number(number: int) -> str:
    """Returns note name by `number`. None if not exists"""
    notes = {i: note for i, note in enumerate(get_all_notes())}
    note = notes.get(number, None)
    if note is None:
        raise NoteNotFoundError("Note not exists :/")
    return note


def get_note_by_name(name: str) -> str:
    """Returns note path by `name`. None if not exists"""
    notes = {get_basename(note): note for note in get_all_notes()}
    note = notes.get(name, None)
    if note is None:
        raise NoteNotFoundError("Note not exists :/")
    return note


def get_all_notes(path=NOTES_PATH) -> list:
    """Returns a list with files in path order by getmtime"""
    files = sorted([os.path.join(path, f) for f in os.listdir(path)],
                   key=os.path.getmtime, reverse=True)
    return files


def get_note(name_or_number):
    """Returns note by name or number in list"""
    try:
        n = int(name_or_number)
        return get_note_by_number(n)
    except ValueError:
        return get_note_by_name(name_or_number)
