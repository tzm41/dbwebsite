#!/usr/bin/python


print "Content-Type: text/html"
print # a blank line must follow the last HTTP headers

import cgi
import cgitb; cgitb.enable()
import time
import random

r = random.randint(0,255)
g = random.randint(0,255)
b = random.randint(0,255)

print """
<title>Hello World!</title>
<body bgcolor="%02x%02x%02x">
<h1>Hello World!</h1>
<p>
This is my first Python web applicaton.
""" % (r,g,b)



print "This page was generated at %s" % time.ctime()


print "</body>"
