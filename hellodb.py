#!/usr/bin/python

import cgi
import cgitb
import MySQLdb as db
import time

cgitb.enable()

print("Content-Type: text/html\n")


def insertName(name, age, student):
    conn = db.connect("localhost", "ztan", "ztan", "ztan")

    cur = conn.cursor()

    sql = "INSERT INTO ztan_db VALUES(%s,%s,%s)"
    params = (name, student, age)

    cur.execute(sql, params)

    print "%d rows were affected" % cur.rowcount

    conn.commit()
    cur.close()
    conn.close()
    print("goodbye!")
    print("<a href='hellodb.py'>Go back</a>")


def printHello(name):
    print """
        <html>
        <body>
        <h1>Hello World CGI!</h1>
        <h2>Hello, {}!!!</h2>

        <p>This page was generated at {}</p>

        </body>
        </html>
        """.format(name, time.ctime())


def printWelcomeForm():
    conn = db.connect("localhost", "ztan", "ztan", "ztan")
    cur = conn.cursor()

    sql = "SELECT * FROM ztan_db"

    cur.execute(sql)
    data = cur.fetchall()
    # print data
    print "<table border=1>"
    for row in data:
        (name, student, age) = row
        print("<tr><td>"
              + name + "</td><td>" + student + "</td><td>"
              + str(age) + "</td></tr>")
    print "</table>"

    cur.close()
    conn.close()

    print """
        <h1>Hello CGI</h1>

        <form method="post">
        Name: <input type="text" name="name"><p>

        <input type="radio" name="student" value="yes">Student<br>
        <input type="radio" name="student" value="no">Non-Student<br>
        <br>
        Age: <input type="text" name="age">
        <br>
        <input type="submit" name="Go!" value="Go!">
        </form>
        """


if __name__ == "__main__":

    # form is a python Dictionary
    form = cgi.FieldStorage()

    # Check if stuff was sent to the program
    if "name" in form and "age" in form and "student" in form:
        # extract the stuff
        name = form["name"].value
        age = int(form["age"].value)
        student = form["student"].value

        # do something with it
        insertName(name, age, student)

    else:
        # no name was sent to the program
        printWelcomeForm()
