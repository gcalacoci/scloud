# -*- coding: utf-8 -*-
"""
    Copyright (C) 2015  Giulio Calacoci <asdmaster@gmail.com>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
import soundcloud
import urllib3
urllib3.disable_warnings()
import sys
from pprint import pprint
import config as c
from jinja2 import Environment, PackageLoader

def custom_urlencode_filter(value):
    try:
#        print >> sys.stderr, value
        return value.encode('utf-8').strip()
    except:
 #       print >> sys.stderr, "errore: %s " % value
        pass

env = Environment(loader=PackageLoader('soundcloud_cli', 'templates'))
env.filters['custom_urlencode_filter'] = custom_urlencode_filter

fname =sys.argv[1]
trks = {}
idx = 1
with open (fname) as f:
    for line in f:
#        l = line.split('-')
        try:
            trks[idx] = line
            idx += 1 
        except:
            continue

# create a client object with your app credentials
client = soundcloud.Client(client_id=c.apikey)
result = {}
#pprint(trks)
for k, v in trks.iteritems():
    try:
#        print v
#        print k
        tracks = client.get('/tracks', q=v.strip())
        result[unicode(v.strip())] = tracks
    except:
        continue
template = env.get_template('scloud_list.html')
print template.render(tracks=result)


#print """
#<!DOCTYPE html>
#<html lang="en">
#  <head>
#    <meta charset="utf-8">
#    <title>title</title>
#    <link rel="stylesheet" href="style.css">
#    <script src="script.js"></script>
#  </head>
#  <body>
#    <!-- page content -->
#    <ul>
#"""
#for v in trks:
#    try:
#        tracks = client.get('/tracks', q=trks[v].strip())
#        print "<li> %s) %s</li>" % (v, trks[v].strip())
#        print "<ul>"
#        for item in tracks:
#           # pprint (item)
#            print '<li>user: %s Search: %s <a href="%s" target="_blank">Link</a> </li>' % (item.user['username'], item.title, item.permalink_url)
#        print "</ul>"
#    except:
#        print "</ul>"
#        continue
#print """</ul>
#  </body>
#</html>
#"""
sys.exit(0)


