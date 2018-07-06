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

def main():
    """ Main routine 
    """

    from Universe import universe
    from Reporting import report, error
    from Support import ReadArguments

    import os

    import ecmwf
    import ncar

    ReadArguments()

    if len(universe.periods) == 0:
        universe.periods.append('201709')
        #universe.periods.append('201708')

    if len(universe.repos) == 0:
        universe.repos.append('ecmwf')
        #universe.repos.append('ncar')

    report('%(blue)sProcessing periods: %(yellow)s%(periods)s%(end)s', var = {'periods': '%(grey)s, %(yellow)s'.join(universe.periods)})
    report('%(blue)sProcessing repos: %(yellow)s%(repos)s%(end)s', var = {'periods': '%(grey)s, %(yellow)s'.join(universe.repos)})
    
    report('%(blue)sOutput to directory: %(yellow)s%(directory)s%(end)s', var = {'directory': universe.directory})

    

    for period in universe.periods:
        report('%(blue)sProcessing period: %(yellow)s%(period)s%(end)s', var = {'period': period})

        if 'ecmwf' in universe.repos:
            report('  %(blue)sProcessing repo: %(yellow)s%(repo)s%(end)s', var = {'repo': 'ecmwf'})
            ecmwf.download(yearmonth=period, folder=universe.directory)

        if 'ncar' in universe.repos:
            report('  %(blue)sProcessing repo: %(yellow)s%(repo)s%(end)s', var = {'repo': 'ncar'})
            ncar.download(yearmonth=period, folder=universe.directory)

