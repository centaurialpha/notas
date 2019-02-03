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
import time
import subprocess
from notas import utils


def new(args):
    """Create new note"""
    _open_editor_with_note(args.name, args.editor)


def _open_editor_with_note(note, editor=None):
    try:
        editor_exec = utils.get_editor(custom_editor=editor)
    except utils.NotEditorFoundError as reason:
        print(reason)
        exit(-1)
    cmd = [editor_exec, utils.get_note_path(note)]
    subprocess.call(cmd)


def open_note(args):
    """Open note"""
    try:
        note = utils.get_note(args.name_number)
    except utils.NoteNotFoundError as reason:
        print(reason)
        exit(-1)
    _open_editor_with_note(note)


def ls(args):
    """Prints all notes"""
    headers = '{:<5} {:<40} {:<40}'.format('#', 'NAME', 'UPDATED')
    print(headers, end='\n\n')
    for count, filename in enumerate(utils.get_all_notes()):
        name = utils.get_basename(filename)
        if len(name) > 35:
            name = '...' + name[-35:]
        updated = time.ctime(os.path.getmtime(filename))
        print('{:<5} {:<40} {:<40}'.format(count, name, updated))
    print()


def rm(args):
    if utils.note_exists(args.name):
        user_input = input("Remove note '{}'? [y/N]: ".format(args.name))
        if user_input in 'yY':
            try:
                utils.remove_note(args.name)
            except utils.NoteNotFoundError as reason:
                print(reason)
                exit(-1)
            else:
                print('Note deleted')
    else:
        print('Note not exists :/')
