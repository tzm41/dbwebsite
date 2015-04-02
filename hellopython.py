#!/usr/bin/python

print "Content-Type: text/html"
print # a blank line must follow the last HTTP headers

import cgi
import cgitb; cgitb.enable()
import time

print "<H1>Hello Python!</H1>"

print "This page was generated at %s" % time.ctime()


