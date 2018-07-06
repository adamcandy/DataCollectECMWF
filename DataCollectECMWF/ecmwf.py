#!/usr/bin/env python

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
from Support import mkdir_p

from ecmwfapi import ECMWFDataServer
from calendar import monthrange

import os

def test(filename='test.nc'):
    server = ECMWFDataServer()
    server.retrieve({
        "class": "ea",
        "dataset": "era5",
        "expver": "1",
        "stream": "oper",
        "type": "an",
        "levtype": "sfc",
        "param": "165.128/166.128/167.128",
        "date": "2016-01-01/to/2016-01-02",
        "time": "00:00:00",
        "step": "0",
        "grid": "0.25/0.25",
        "area": "75/-20/10/60",
        "format": "netcdf",
        "target": filename,
     })

def download(filename=None, yearmonth='201708', fformat=None, folder='./'):
    year  = int(yearmonth[0:4])
    month = int(yearmonth[4:6])
    #date  = int(yearmonthdate[6:8])
    end_date = monthrange(year, month)[-1]

    if not filename:
        filename = 'ecmwf-era5-winds10m-%(yearmonth)s.nc' % {
            'yearmonth': yearmonth,
        }

    if not os.path.exists(os.path.abspath(folder)):
        mkdir_p(os.path.abspath(folder))

    fullname = os.path.join(os.path.abspath(folder), filename)

    spec = {
        "class": "ea",
        "dataset": "era5",
        #"date": "%(year)d%(month)d01/%(year)d%(month)d%(date)d" % {
        "date": "%(year)d-%(month)d-01/to/%(year)d-%(month)d-%(date)d" % {
            'year':  year,
            'month': month,
            'date':  end_date,
        },
        "expver": "1",
        "levtype": "sfc",
        "number": "0/1/2/3/4/5/6/7/8/9",
        "param": "165.128/166.128",
        #"stream": "oper",
        "stream": "enda",
        "time": "00:00:00/03:00:00/06:00:00/09:00:00/12:00:00/15:00:00/18:00:00/21:00:00",
        "type": "an",
        "step": "0",
        #"grid": "0.25/0.25",
        "area": "46/-100/5/-50",  # North/West/South/East
        #"format": "netcdf",
        "target": fullname,
    }
    if fformat:
        spec['format'] = fformat
        # Requires grid spec?
        #    See: https://software.ecmwf.int/wiki/display/CKB/Global+data%3A+Download+data+from+ECMWF+for+a+particular+area+and+resolution
    print 'ECMWF ERA5 Collect for period %(period)s, output to: %(fullname)s' % {
        'filename': fullname,
        'period': spec['date'],
    }
    if not universe.dry:
        server = ECMWFDataServer()
        server.retrieve(spec)

fformat = None
#fformat = 'netcdf'

def test():
    download(yearmonth='201709', folder='../test/')


if __name__ == '__main__':
    sys.exit(test())

