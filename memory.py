#!/usr/bin/python
print "Content-Type: text/html\n"
print ""

import cgi
import cgitb
from datetime import datetime
cgitb.enable()

fs = cgi.FieldStorage()

long_term = open('memory.csv', 'a')
short_term = fs['memory'].value.split('\n')
now = str(datetime.today())

for entry in short_term:
    long_term.write(entry+now+'\n')
long_term.close()
