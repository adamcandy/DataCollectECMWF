#!/usr/bin/env python
# -*- coding: utf-8 -*-

##########################################################################
#  
#  DataCollectECMWF
#
#  Project to interact with external data libraries, including ECMWF, NCAS, ...
#  
#  Copyright (C) 2018- Dr Adam S. Candy, adam@candylab.org
#  
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
#  
##########################################################################

import os

colour = {
    'red', None,
    'green', None,
    'blue', None,
    'cyan', None,
    'magenta', None,
    'brightred', None,
    'brightgreen', None,
    'brightmagenta', None,
    'brightyellow', None,
    'brightcyan', None,
    'yellow', None,
    'bred', None,
    'bcyan', None,
    'bblue', None,
    'bmagenta', None,
    'byellow', None,
    'bgreen', None,
    'bwhite', None,
    'grey', None,
    'fred', None,
    'end', None,
}

class universe():
    verbose = True
    debug = False
    dry = False
    periods = []
    repos = []
    directory = './'

