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

import sys
import os
from Universe import universe

def usage(unknown = None):
    if unknown:
        print 'Unknown option ' + unknown
    print '''Usage for %(cmdname)s
 %(cmdname)s [options] (filename)
- Options ---------------------\ 
   -m (YYYYMM)                 | Specify month period  (multiple -d permitted)
   -r (repo)                   | Specify repository names, e.g. 'ecmwf', 'ncar', ...  (multiple -r permitted)
   -f (folder)                 | Specify output folder 
                               |_________________________________________________________________________________
   -h                          | Help
   -d                          | Dry run
   -v                          | Verbose
   -vv                         | Very verbose (debugging)
   -q                          | Quiet
                               \__________________________________________________________________________________''' % { 'cmdname': os.path.basename(sys.argv[0]) }
    sys.exit(1)

