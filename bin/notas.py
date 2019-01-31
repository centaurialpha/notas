#!/usr/bin/env python3
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
"""Entry point"""

import sys
from notas import cli


def main():
    parser = cli.cliparse()
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)
    args = parser.parse_args()
    if 'slot' in args:
        args.slot(args)


if __name__ == '__main__':
    main()