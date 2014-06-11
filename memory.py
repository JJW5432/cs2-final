#!/usr/bin/python

import cgi

fs = cgi.FieldStorage()

f = File.open('memory.csv', 'a')
f.write(fs['memory'].value)
f.close()