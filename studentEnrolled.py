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


def acquireResult(cname):
    data = dba.showCourseStudent(cname)
    if data is not None:
        result = []
        result.append('<table id="tables"><tr><th>Student</th></tr>')
        for course in data:
            result.append('<tr class="alt"><td>' + course[0] + "</td></tr>")
        result.append("</table>")
        return ''.join(result)
    else:
        return '<h2>Course {} is not found.</h2>'.format(cname)


def printResult(cname):
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
        <h1><a href="#">Students enrolled in {}</a></h1>
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
        """.format(cname, acquireResult(cname), time.ctime())))


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
        <h1><a href="#">Student List of a Course</a></h1>
        </div>

        <div id="content">
        <form method="post">
        <h1>Course name: </h1>
        <input type="text" name="cname">
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
    if "cname" in form:
        cname = form["cname"].value
        printResult(cname)
    else:
        printForm()
