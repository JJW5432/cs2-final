#!/usr/bin/python
print ""

import cgi

fs = cgi.FieldStorage()

f = File.open('memory.csv', 'a')
f.write(fs['memory'].value)
f.close()