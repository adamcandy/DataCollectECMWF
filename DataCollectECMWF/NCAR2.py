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

def install_basic_client_local(uri='', user='', passwd='', use_netrc=True):

    import cookielib
    import netrc
    import urllib2
    import re
     
    import pydap.lib
    from pydap.exceptions import ClientError
     
    import logging
     
    log = logging.getLogger(__name__)
    log.setLevel(logging.DEBUG)
     
    # Set the debug level for urllib2.
    debuglevel=1
     
    # ---------------------------------------------------------------

    # Create special opener with support for Cookies
    cj = cookielib.CookieJar()
    
    # Create the password manager and load with the credentials using 
    pwMgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
 
    # Get passwords from the .netrc file nless use_netrc is False    
    if use_netrc:
        logins = netrc.netrc()
        accounts = logins.hosts # a dist of hosts and tuples
        for host, info in accounts.iteritems():
            login, account, password = info
            log.debug('Host: %s; login: %s; account: %s; password: %s' % (host, login, account, password))
            pwMgr.add_password(None, host, login, password)
        
    if uri and user and passwd:
        pwMgr.add_password(None, uri, user, passwd)
    
    opener = urllib2.build_opener(urllib2.HTTPBasicAuthHandler(pwMgr),
                                  urllib2.HTTPCookieProcessor(cj))
    
    opener.addheaders = [('User-agent', 'pydap/EL')]
 
    urllib2.install_opener(opener)
 
    def new_request(url):
        if url[-1] is '&': url = url[0:-1]
        log.debug('Opening %s (install_basic_client)' % url)
        r = urllib2.urlopen(url)
        
        resp = r.headers.dict
        resp['status'] = str(r.code)
        data = r.read()
 
        # When an error is returned, we parse the error message from the
        # server and return it in a ``ClientError`` exception.
        if resp.get("content-description") == "dods_error":
            m = re.search('code = (?P<code>\d+);\s*message = "(?P<msg>.*)"',
                    data, re.DOTALL | re.MULTILINE)
            msg = 'Server error %(code)s: "%(msg)s"' % m.groupdict()
            raise ClientError(msg)
 
        return resp, data
 
    from pydap.util import http
    http.request = new_request
    
# END BASIC AUTH MODULE CODE
 
try:
    from pydap.util.urs import install_basic_client
except:
    print 'Failed to load global: from pydap.util.urs import install_basic_client'
    install_basic_client = install_basic_client_local

install_basic_client()
from pydap.client import open_url
dataset = open_url('https://rda.ucar.edu/thredds/dodsC/files/g/ds094.1/2017/wnd10m.cdas1.201708.grb2')
 
