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


def printResult(name, course, cred):
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
        <h1><a href="#">Enroll {} into {} for {}</a></h1>
        </div>

        <div id="content">
        <h2>{}</h2>
        <h2><a href="university.py">Back to main</a></h2>
        </div>

        <div id="footer">
        <p>This page was generated at {}</p
        <P>Colin Tan</p>
        </div>
        </div>
        </body>
        </html>
        """.format(name, course, cred,
                   dba.enrollCourse(course, name, cred), time.ctime())))


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
        <h1><a href="#">Enroll a student into a course</a></h1>
        </div>

        <div id="content">
        <form method="post">
        <h1>Name: </h1>
        <input type="text" name="name">
        <h1>Course: </h1>
        <input type="text" name="course">
        <h1>Credit status: </h1>
        <input type="text" name="cred">
        <input type="submit" name="Go!" value="Go!">
        </form>
        <h2><a href="studentList.py">List students</a></h2>
        <h2><a href="courseEnrolled.py">List student's courses</a></h2>
        <h2><a href="studentEnrolled.py">List course's students</a></h2>
        <h2><a href="courseEnrolled.py">List student's courses</a></h2>
        <h2><a href="studentEnrolled.py">List course's students</a></h2>
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
    if "name" in form and "course" in form:
        name = form["name"].value
        course = form["course"].value
        cred = form["cred"].value
        printResult(name, course, cred)
    else:
        printForm()
