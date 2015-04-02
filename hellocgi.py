#!/usr/bin/python

import cgi
import cgitb
import time
cgitb.enable()

print "Content-Type: text/html\n"


def printHello(name):
    print """
<html>
<body>
<h1>Hello World CGI!</h1>
<h2>Hello, %s!!!</h2>

<p>
This page was generated at %s
</p>

</body>
</html>
""" % (name, time.ctime())


def printWelcomeForm():

    print """

<h1>Hello CGI</h1>

<form method="post">
Name: <input type="text" name="name"><p>

<input type="radio" name="student" value="yes"> Student<br>
<input type="radio" name="student" value="no"> Non-Student<br>


<input type="submit" name="Go!" value="Go!">
</form>





"""


if __name__ == "__main__":

    # form is a python Dictionary
    form = cgi.FieldStorage()

    # Check if stuff was sent to the program
    if form.has_key("name"):
        # extract the stuff
        name = form["name"].value

        # do something with it
        printHello(name)

    else:
        # no name was sent to the program
        printWelcomeForm()

