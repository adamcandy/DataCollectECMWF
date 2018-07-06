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

def download(filename=None, yearmonth='201708', field='wind', fformat=None):
    from pydap.client import open_url                                               
    from pydap.cas.urs import setup_session                                         

    year  = int(yearmonth[0:4])
    month = int(yearmonth[4:6])
    #date  = int(yearmonthdate[6:8])
    end_date = monthrange(year, month)[-1]

    #https://rda.ucar.edu/thredds/dodsC/files/g/ds094.1/2017/prmsl.cdas1.201708.grb2
    #https://rda.ucar.edu/thredds/dodsC/files/g/ds094.1/2017/prmsl.cdas1.201709.grb2

    #https://rda.ucar.edu/thredds/dodsC/files/g/ds094.1/2017/wnd10m.cdas1.201708.grb2
    #https://rda.ucar.edu/thredds/dodsC/files/g/ds094.1/2017/wnd10m.cdas1.201709.grb2

    if field == 'wind':
        url = 'https://rda.ucar.edu/thredds/dodsC/files/g/ds094.1/%(year)d/wnd10m.cdas1.%(year)d%(month)d.grb2' % {
            'year':  year,
            'month': month,
        } 
    else:
        url = 'https://rda.ucar.edu/thredds/dodsC/files/g/ds094.1/%(year)d/prmsl.cdas1.%(year)d%(month)d.grb2' % {
            'year':  year,
            'month': month,
        } 

    session = setup_session(username, password, check_url=url2)                     
    data = open_url(url, session=session)
                                     
    print(data['time'].shape)                                                          
    #print(ds2['time'][0, 0, 0])                                                       
    #print(ds3['time'].shape)                                                           
    #print(ds3['time'][0, 0, 0, 0])     


def test():
    #download(yearmonth='201709')

if __name__ == '__main__':
    sys.exit(test())





