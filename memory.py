#!/usr/bin/python
print ""

import cgi
import cgitb
cgitb.enable()

fs = cgi.FieldStorage()

f = open('memory.csv', 'a')
f.write(fs['memory'].value)
f.close()
