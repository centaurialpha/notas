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
"""Simple tool to create, list and delete notes using the default editor"""
import argparse

from notas import functions


def cliparse():
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers()
    # Nueva nota
    new_note = subparsers.add_parser('new', help='Create new note')
    new_note.add_argument('name')
    new_note.add_argument('-e', '--editor', help='Use this editor')
    new_note.set_defaults(slot=functions.new)
    # Listado
    ls_note = subparsers.add_parser('ls', help='List all notes')
    ls_note.set_defaults(slot=functions.ls)
    # Open
    open_note = subparsers.add_parser('open', help='Open note')
    open_note.add_argument('name_number')
    open_note.set_defaults(slot=functions.open_note)
    # Remove
    rm_note = subparsers.add_parser('rm', help='Remove notes')
    rm_note.add_argument('name')
    rm_note.set_defaults(slot=functions.rm)
    return parser
