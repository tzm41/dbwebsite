#!/usr/bin/env python
import cgi
import cgitb
import time
import textwrap
import dbaccess as dba

cgitb.enable()
print("Content-Type: text/html\n")

__author__ = 'Colin Tan'
__version__ = '1.3'


def printResult(name, major):
    print(textwrap.dedent("""
        <!DOCTYPE html>
        <html>
        <head>
        <link rel="stylesheet" type="text/css" href="css/style.css">
        <title>University Database</title>
        </head>

        <body>
        <div id="wrap">
        <div id="header">
        <h1><a href="#">Update Major of {}</a></h1>
        </div>

        <div id="content">
        <h2>{}</h2>
        <h2><a href="showMajor.py">Show major of students</a></h2>
        <h2><a href="university.py">Back to main</a></h2>
        </div>

        <div id="footer">
        <p>This page was generated at {}</p
        <P>Colin Tan</p>
        </div>
        </div>
        </body>
        </html>
        """.format(name, dba.updateMajor(name, major), time.ctime())))


def printForm():
    print(textwrap.dedent("""
        <!DOCTYPE html>
        <html>
        <head>
        <link rel="stylesheet" type="text/css" href="css/style.css">
        <title>University Database</title>
        </head>

        <body>
        <div id="wrap">
        <div id="header">
        <h1><a href="#">Update/Add Major of a Student</a></h1>
        </div>

        <div id="content">
        <form method="post">
        <h1><a href="studentList.py">Name (click to view): </a></h1>
        <input type="text" name="name">
        <h1>New major: </h1>
        <input type="text" name="major">
        <input type="submit" name="Go!" value="Go!">
        </form>
        <h2><a href="showMajor.py">Show major of students</a></h2>
        <h2><a href="university.py">Back to main</a></h2>
        </div>

        <div id="footer">
        <p>This page was generated at {}</p
        <P>Colin Tan</p>
        </div>
        </div>
        </body>
        </html>
        """.format(time.ctime())))


if __name__ == "__main__":
    form = cgi.FieldStorage()
    if "name" in form and "major" in form:
        name = form["name"].value
        major = form["major"].value
        printResult(name, major)
    else:
        printForm()
