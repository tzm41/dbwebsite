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


def acquireResult(name):
    data = dba.showCourseEnrolled(name)
    if data is not None:
        result = []
        result.append('<table id="tables"><tr><th>Course</th></tr>')
        for course in data:
            result.append('<tr class="alt"><td>' + course[0] + "</td></tr>")
        result.append("</table>")
        return ''.join(result)
    else:
        return '<h2>Student {} is not found.</h2>'.format(name)


def printResult(name):
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
        <h1><a href="#">Course Enrolled by {}</a></h1>
        </div>

        <div id="content">
        {}
        <h2><a href="university.py">Back to main</a></h2>
        </div>

        <div id="footer">
        <p>This page was generated at {}</p
        <P>Colin Tan</p>
        </div>
        </div>
        </body>
        </html>
        """.format(name, acquireResult(name), time.ctime())))


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
        <h1><a href="#">Course List of a Student</a></h1>
        </div>

        <div id="content">
        <form method="post">
        <h1><a href="studentList.py">Name (click to view): </a></h1>
        <input type="text" name="name">
        <input type="submit" name="Go!" value="Go!">
        </form>
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
    if "name" in form:
        name = form["name"].value
        printResult(name)
    else:
        printForm()
