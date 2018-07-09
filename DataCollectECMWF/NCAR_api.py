#!/usr/bin/env python

##########################################################################
#  
#  DataCollectECMWF
#
#  Project to interact with external data libraries, including ECMWF, NCAS, ...
#  
#  Copyright (C) 2018- Dr Adam S. Candy, a.s.candy@tudelft.nl, adam@candylab.org
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

import configparser
import os

class NCAR_Auth(object):

    _config_filename = '~/.ncarapirc'

    def __init__(self):
        self.Read()        

    def Read(self):
        config = configparser.ConfigParser()
        #config.sections()
        config.read(os.path.expanduser(self._config_filename))
        self.username = config['default']['username']
        self.password = config['default']['password']


