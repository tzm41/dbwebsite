#!/usr/bin/env python
import cgi
import cgitb
import time
# import dbaccess as dba

cgitb.enable()
print("Content-Type: text/html\n")

__author__ = 'Colin Tan'
__version__ = '1.2'


def printWelcome():
    print("""
        <html>
        <body>
        <h1>Welcome to the university database!</h1>

        <p>This page was generated at {}</p
        <P>Colin Tan</p>
        </body>
        </html>
        """.format(time.ctime()))


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
    # form is a python Dictionary
    # form = cgi.FieldStorage()

    printWelcome()
