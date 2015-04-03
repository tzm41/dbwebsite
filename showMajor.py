#!/usr/bin/env python
import cgitb
import time
import textwrap
import dbaccess as dba

cgitb.enable()
print("Content-Type: text/html\n")

__author__ = 'Colin Tan'
__version__ = '1.3'


def acquireResult():
    data = dba.displayMajorOfStudents()
    result = []
    result.append('<table id="tables"><tr><th>Student</th><th>Major</th></tr>')
    for student in data:
        name, dept = student
        result.append('<tr class="alt"><td>'
                      + name + "</td><td>" + dept + "</td></tr>")
    result.append("</table>")
    return ''.join(result)


def printResult():
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
        <h1><a href="#">Student Major</a></h1>
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
        """.format(acquireResult(), time.ctime())))


if __name__ == "__main__":
    printResult()
