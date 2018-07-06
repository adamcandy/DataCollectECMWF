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

from Universe import universe, colour

colours_pretty = {
    'red':'\033[0;31m',
    'green':'\033[0;32m',
    'blue':'\033[0;34m',
    'cyan':'\033[0;36m',
    'magenta':'\033[0;35m',
    'brightred':'\033[1;31m',
    'brightgreen':'\033[1;32m',
    'brightmagenta':'\033[1;35m',
    'brightyellow':'\033[1;33m',
    'brightcyan':'\033[1;36m',
    'yellow':'\033[0;33m',
    'bred':'\033[7;31m',
    'bcyan':'\033[7;36m',
    'bblue':'\033[7;34m',
    'bmagenta':'\033[7;35m',
    'byellow':'\033[7;33;40m',
    'bgreen':'\033[7;32m',
    'bwhite':'\033[7;37m',
    'grey':'\033[1;30m',
    'fred':'\033[5;31m',
    'end':'\033[0m'
}

colours_plain = {}
for colour in colours_pretty.keys():
    colours_plain[colour] = ''

def merge(*dict_args):
    '''
    Given any number of dicts, shallow copy and merge into a new dict,
    precedence goes to key value pairs in latter dicts.
    '''
    result = {}
    for dictionary in dict_args:
        result.update(dictionary)
    return result

def addcolour(dic, colourful = True):
    result = {}
    if colourful:
        result.update(colours_pretty)
    else:
        result.update(colours_plain)
    result.update(dic)
    return result

def report(text, var = {}, debug = False, force = False, colourful = True, indent=0, include=True, test=False):
    # Link to rep.report
    # Option to send to log file instead - independent of terminal verbosity
    if debug and not universe.debug:
        return
    spacer = ' ' * 2 * indent
    suffix = ''
    if debug:
        suffix = '  %(grey)s[DEBUG]%(end)s'
    if universe.verbose or force or (universe.testfolder is not None and test):
        print((spacer + text + suffix) % addcolour(var, colourful = colourful))
    if universe.log is not None:
        universe.log.Write(spacer + text % addcolour(var, colourful = False))

def error(text, var = {}, fatal=False, warning=False):
    suffix = ''
    prefix = 'ERROR'
    if fatal:
        suffix = '%(brightred)s  [FATAL]%(end)s'
    if warning:
        prefix = 'WARNING'
    report('%(brightred)s' + prefix + ':%(end)s %(red)s' + text + '%(end)s' + suffix, var=var, force=True)
    if fatal:
        if universe.debug:    
            raise Exception('Fatal error: ' + text)
        else:
            from sys import exit
            exit(1)


