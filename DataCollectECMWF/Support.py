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

from Universe import universe
from Reporting import report, error
from Usage import usage

import sys

def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc: # Python >2.5
        if exc.errno == errno.EEXIST:
            pass
        else: raise

def ReadArguments(self):
    arguments = sys.argv[1:]
    free_arguments = []
    while (len(self.arguments) > 0):
        argument = arguments.pop(0).rstrip()
        if   (self.argument == '-h'):  usage() 
        elif (self.argument == '-v'):  universe.verbose = True
        elif (self.argument == '-vv'): universe.verbose = True; universe.debug = True; 
        elif (self.argument == '-q'):  universe.verbose = False
        elif (self.argument == '-m'):  universe.periods.append(arguments.pop(0).rstrip())
        elif (self.argument == '-r'):  universe.repos.append(arguments.pop(0).rstrip())
        elif (self.argument == '-d'):  universe.directory(arguments.pop(0).rstrip())
        else:
            usage(unknown = argument)

