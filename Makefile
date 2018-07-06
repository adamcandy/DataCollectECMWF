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

ECHO=echo

default: bin/DataCollectECMWF

bin/cyril: src/DataCollectECMWF
	@mkdir -p bin
	@cp src/DataCollectECMWF bin/DataCollectECMWF

clean:
	@echo 'CLEAN DataCollectECMWF'
	@rm -f DataCollectECMWF/*.pyc
	@echo 'CLEAN bin'
	@rm -rf bin

# ------------------------------------------------------------------------

.PHONY: clean default

.FORCE: 

# ------------------------------------------------------------------------

