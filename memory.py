#!/usr/bin/python
print ""

import cgi
import cgitb
from datetime import datetime
cgitb.enable()

fs = cgi.FieldStorage()

f = open('memory.csv', 'a')
f.write(fs['memory'].value+str(datetime.today())
f.close()
