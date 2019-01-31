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

from setuptools import setup, find_packages


setup(
    name='notas',
    version='0.1',
    author='Gabriel Acosta',
    author_email='acostadariogabriel@gmail.com',
    python_requires='>=3',
    # long_description=''
    packages=find_packages(exclude=['tests']),
    entry_points={
        'console_scripts': ['notas=bin.notas:main']
    }
)
