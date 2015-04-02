#!/usr/bin/env python
import MySQLdb as db

__author__ = 'Colin Tan'
__version__ = '1.2'


# Displays a list of all students from the database.
def displayStudentList():
    "Displays number of majors in each department."
    conn = db.connect("localhost", "ztan", "ztan", "ztan_university")
    cursor = conn.cursor()
    sql = "SELECT * FROM Student"
    cursor.execute(sql)
    data = cursor.fetchall()
    conn.close()
    return data


# Displays number of majors in each department.
def displayMajorInDept():
    "Displays number of majors in each department."
    conn = db.connect("localhost", "ztan", "ztan", "ztan_university")
    cursor = conn.cursor()
    sql = """SELECT name, IFNULL(numstudents, 0)
        FROM department
        LEFT OUTER JOIN
        (SELECT dept, COUNT(student) AS numstudents
        FROM MajorsIn
        GROUP BY dept)
        ON dept== name;"""
    cursor.execute(sql)

    data = cursor.fetchall()
    print("Dept name".ljust(15) + "Number".ljust(15))
    for dept in data:
        name, num = dept
        print(name.ljust(15) + str(num).ljust(15))
    conn.close()


# Show course enrolled by a student
def showCourseEnrolled(name):
    "Show course enrolled by a student"
    conn = db.connect("localhost", "ztan", "ztan", "ztan_university")
    cursor = conn.cursor()

    name_param = (name,)
    get_name = """SELECT id
        FROM Student
        WHERE name = ?"""
    cursor.execute(get_name, name_param)
    id = cursor.fetchone()
    if id is None:
        print("Student not found.")
    else:
        get_course = """SELECT course
            FROM Enrolled
            WHERE student = {}""".format(id[0])
        cursor.execute(get_course)
        course = cursor.fetchall()
        if course is None:
            print("No course enrolled by {} is found.".format(name))
        else:
            print("Course enrolled by {}".format(name).ljust(15))
            for cname in course:
                print(cname[0].ljust(15))
    conn.close()


# Update major of a student
def updateMajor(name, major):
    "Update major of a student"
    conn = db.connect("localhost", "ztan", "ztan", "ztan_university")
    cursor = conn.cursor()

    name_param = (name,)
    get_name = """SELECT id
        FROM Student
        WHERE name = ?"""
    cursor.execute(get_name, name_param)
    id = cursor.fetchone()
    if id is None:
        print("Student not found.")
    else:
        update_major = """UPDATE MajorsIn
        SET dept = ?
        WHERE student = {}""".format(id[0])

        maj_param = (major,)
        cursor.execute(update_major, maj_param)
        conn.commit()
        if cursor.rowcount > 0:
            print "Succeeded."
        else:
            print "Failed. No rows updated. (Probably major not declared yet.)"
    conn.close()


# Show course's enrolled students
def showCourseStudent(cname):
    "Show course's enrolled students"
    conn = db.connect("localhost", "ztan", "ztan", "ztan_university")
    cursor = conn.cursor()

    sql = """SELECT name
        FROM Enrolled, Student
        WHERE Enrolled.course = ? AND Student.id = Enrolled.Student;"""
    params = (cname,)
    cursor.execute(sql, params)
    student = cursor.fetchall()
    if student is None:
        print "No student enrolled or no such course."
    else:
        print("Enrolled student of {}".format(cname).ljust(15))
        for name in student:
            print(name[0].ljust(15))
    conn.close()


# Add a student into the database
def addStudent(ID, name):
    "Add a student into the database."
    conn = db.connect("localhost", "ztan", "ztan", "ztan_university")
    cursor = conn.cursor()

    sql = "INSERT INTO Student VALUES (?,?)"
    params = (ID, name)
    cursor.execute(sql, params)
    conn.commit()
    if cursor.rowcount > 0:
        print "Succeeded."
    else:
        print "Failed."
    conn.close()


# Delete a room
def delRoom(rname):
    "Delete a room"
    conn = db.connect("localhost", "ztan", "ztan", "ztan_university")
    cursor = conn.cursor()

    param = (rname,)
    sql = "DELETE FROM Room WHERE name = ?"
    cursor.execute(sql, param)
    conn.commit()
    if cursor.rowcount > 0:
        print "Succeeded."
    else:
        print "Failed. No rows updated. (Probably no such a room.)"
    conn.close()


# Deroll a student from a course
def delReg(name, course):
    "Deroll a student from a course"
    conn = db.connect("localhost", "ztan", "ztan", "ztan_university")
    cursor = conn.cursor()

    param = (name, course)
    sql = """DELETE FROM Enrolled
        WHERE Enrolled.student IN (SELECT id
        FROM student
        WHERE name = ?) AND course = ?;"""
    cursor.execute(sql, param)
    conn.commit()
    if cursor.rowcount > 0:
        print "Succeeded."
    else:
        print "Failed. No rows updated. (Probably no such a record.)"
    conn.close()


# Enrolled student into a class
def enrollCourse(course, name, cred):
    "Enrolled student into a class."
    conn = db.connect("localhost", "ztan", "ztan", "ztan_university")
    cursor = conn.cursor()

    name_param = (name,)
    get_name = """SELECT id
        FROM Student
        WHERE name = ?"""
    cursor.execute(get_name, name_param)
    id = cursor.fetchone()
    if id is None:
        print("Student not found.")
    else:
        enroll = "INSERT INTO Enrolled VALUES (?,?,?);"

        cor_param = (id[0], course, cred)
        cursor.execute(enroll, cor_param)
        conn.commit()
        if cursor.rowcount > 0:
            print "Succeeded."
        else:
            print "Failed. No rows updated."
    conn.close()
