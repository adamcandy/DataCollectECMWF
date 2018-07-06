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

import sys, os

def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc: # Python >2.5
        if exc.errno == errno.EEXIST:
            pass
        else: raise

def pretty(d, indent=0):
   for key, value in d.items():
      print('\t' * indent + str(key))
      if isinstance(value, dict):
         pretty(value, indent+1)
      else:
         print('\t' * (indent+1) + str(value))

def ReadArguments():
    arguments = sys.argv[1:]
    free_arguments = []
    while (len(arguments) > 0):
        argument = arguments.pop(0).rstrip()
        if   (argument == '-h'):  usage() 
        elif (argument == '-v'):  universe.verbose = True
        elif (argument == '-vv'): universe.verbose = True; universe.debug = True; 
        elif (argument == '-q'):  universe.verbose = False
        elif (argument == '-d'):  universe.dry = True
        elif (argument == '-m'):  universe.periods.append(arguments.pop(0).rstrip())
        elif (argument == '-r'):  universe.repos.append(arguments.pop(0).rstrip())
        elif (argument == '-f'):  universe.folder = arguments.pop(0).rstrip()
        else:
            usage(unknown = argument)

