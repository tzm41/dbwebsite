#!/usr/bin/env python
import cgitb
import time
import textwrap

cgitb.enable()
print("Content-Type: text/html\n")

__author__ = 'Colin Tan'
__version__ = '1.4'


def printWelcome():
    links = '''
    <h2><a href="studentList.py">List students</a></h2>
    <h2><a href="majorInDept.py">List majors in each department</a></h2>
    <h2><a href="courseEnrolled.py">List student's courses</a></h2>
    <h2><a href="studentEnrolled.py">List course's students</a></h2>
    <h2><a href="updateMajor.py">Update/Add major of a student</a></h2>
    <h2><a href="deleteReg.py">Deroll a student from a course</a></h2>
    <h2><a href="addReg.py">Enroll a student into a course</a></h2>
    <h2><a href="showMajor.py">Show major of students</a></h2>
    <h2><a href="addStudent.py">Add a student into the database</a></h2>
    <h2><a href="deleteRoom.py">Delete a room</a></h2>'''

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
        <h1><a href="#">Welcome to the university database!</a></h1>
        </div>

        <div id="intro">
        <p>Online version of the university database.</p>
        <p>Interactive functions.</p>
        </div>

        <div id="content">
        <div class="article">
        </div>
        {}
        </div>

        <div id="footer">
        <p>This page was generated at {}</p
        <P>Colin Tan</p>
        </div>
        </div>
        </body>
        </html>
        """.format(links, time.ctime())))


def main():
    choice = "foo"
    while choice.lower()[0] != "q":
        choice = raw_input("> ")
        if choice.lower()[0] == "d":
            dba.displayStudentList()
        elif choice.lower()[0] == "p":
            dba.displayMajorInDept()
        elif choice.lower()[0] == "t":
            name = raw_input("Enter name of student: ")
            dba.showCourseEnrolled(name)
            course = raw_input("Enter name of couse: ")
            dba.delReg(name, course)
        elif choice.lower()[0] == "c":
            name = raw_input("Enter name of student: ")
            dba.showCourseEnrolled(name)
        elif choice.lower()[0] == "u":
            name = raw_input("Enter name of student: ")
            major = raw_input("Enter new major: ")
            dba.updateMajor(name, major)
        elif choice.lower()[0] == "f":
            cname = raw_input("Enter name of course: ")
            dba.showCourseStudent(cname)
        elif choice.lower()[0] == "a":
            iden = raw_input("Enter ID of student: ")
            name = raw_input("Enter name of student: ")
            dba.addStudent(iden, name)
        elif choice.lower()[0] == "e":
            course = raw_input("Enter name of couse: ")
            name = raw_input("Enter name of student: ")
            cred = raw_input("Enter credit status: ")
            dba.enrollCourse(course, name, cred)
        elif choice.lower()[0] == "r":
            rname = raw_input("Enter name of room: ")
            dba.delRoom(rname)
        elif choice.lower()[0] == "q":
            print "Goodbye!"
            raise SystemExit

if __name__ == "__main__":

    printWelcome()
