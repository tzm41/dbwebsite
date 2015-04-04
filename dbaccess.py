#!/usr/bin/env python
import MySQLdb as db

__author__ = 'Colin Tan'
__version__ = '1.3'


# Return a list of all students from the database
def displayStudentList():
    "Return a list of all students from the database."
    conn = db.connect("localhost", "ztan", "ztan", "ztan_university")
    cursor = conn.cursor()
    sql = "SELECT * FROM Student;"
    cursor.execute(sql)
    data = cursor.fetchall()
    conn.close()
    return(data)


# Return a list of all majors from the database
def displayMajorList():
    "Return a list of all students from the database."
    conn = db.connect("localhost", "ztan", "ztan", "ztan_university")
    cursor = conn.cursor()
    sql = "SELECT name FROM Department;"
    cursor.execute(sql)
    data = cursor.fetchall()
    conn.close()
    return(data)


# Return number of majors in each department
def displayMajorInDept():
    "Return number of majors in each department."
    conn = db.connect("localhost", "ztan", "ztan", "ztan_university")
    cursor = conn.cursor()
    sql = """SELECT dept AS alias, COUNT(student) AS numstudents
        FROM MajorsIn
        GROUP BY dept;
        SELECT name, IFNULL(numstudents, 0)
        FROM department
        LEFT OUTER JOIN
        alias
        ON alias.dept == name;"""
    cursor.execute(sql)
    data = cursor.fetchall()
    conn.close()
    return(data)


# Return major of each student
def displayMajorOfStudents():
    "Return major of each student."
    conn = db.connect("localhost", "ztan", "ztan", "ztan_university")
    cursor = conn.cursor()
    sql = """SELECT name, dept
        FROM MajorsIn JOIN Student
        ON MajorsIn.student = Student.id;"""
    cursor.execute(sql)
    data = cursor.fetchall()
    conn.close()
    return(data)


# Return course enrolled by a student
def showCourseEnrolled(name):
    "Return course enrolled by a student"
    conn = db.connect("localhost", "ztan", "ztan", "ztan_university")
    cursor = conn.cursor()
    get_name = """SELECT id
        FROM Student
        WHERE name = %s;"""
    cursor.execute(get_name, name)
    id = cursor.fetchone()
    if id is not None:
        get_course = """SELECT course
            FROM Enrolled
            WHERE student = {};""".format(id[0])
        cursor.execute(get_course)
        course = cursor.fetchall()
        conn.close()
        return(course)
    else:
        return(None)


# Update major of a student
def updateMajor(name, major):
    "Update major of a student"
    conn = db.connect("localhost", "ztan", "ztan", "ztan_university")
    cursor = conn.cursor()
    get_id = """SELECT id
        FROM Student
        WHERE name = %s;"""
    cursor.execute(get_id, name)
    id = cursor.fetchone()
    if id is None:
        conn.close()
        return("Student not found.")
    else:
        update_major = """UPDATE MajorsIn
            SET dept = %s
            WHERE student = {};""".format(id[0])
        cursor.execute(update_major, major)
        conn.commit()
        if cursor.rowcount > 0:
            conn.close()
            return("Updated major of {} to {}.".format(name, major))
        else:
            conn.close()
            return addMajor(id, major)


# fallback adding major of a student
def addMajor(id, major):
    "Add major of a student"
    conn = db.connect("localhost", "ztan", "ztan", "ztan_university")
    cursor = conn.cursor()
    add_major = "INSERT INTO MajorsIn VALUES({}, %s);".format(id[0])
    cursor.execute(add_major, major)
    conn.commit()
    if cursor.rowcount > 0:
        conn.close()
        return("Successfully added major {} to the student.".format(major))
    else:
        conn.close()
        return("Failed. No rows updated.")


# Show course's enrolled students
def showCourseStudent(cname):
    "Show course's enrolled students"
    conn = db.connect("localhost", "ztan", "ztan", "ztan_university")
    cursor = conn.cursor()

    sql = """SELECT name
        FROM Enrolled, Student
        WHERE Enrolled.course = %s AND Student.id = Enrolled.Student;"""
    cursor.execute(sql, cname)
    student = cursor.fetchall()
    conn.close()
    return student


# Add a student into the database
def addStudent(ID, name):
    "Add a student into the database."
    conn = db.connect("localhost", "ztan", "ztan", "ztan_university")
    cursor = conn.cursor()

    sql = "INSERT INTO Student VALUES (%s, %s);"
    cursor.execute(sql, (ID, name))
    conn.commit()
    row = cursor.rowcount
    conn.close()
    if row > 0:
        return("Succeeded.")
    else:
        return("Failed.")


# Delete a room
def delRoom(rname):
    "Delete a room"
    conn = db.connect("localhost", "ztan", "ztan", "ztan_university")
    cursor = conn.cursor()

    sql = "DELETE FROM Room WHERE name = %s;"
    cursor.execute(sql, rname)
    conn.commit()
    if cursor.rowcount > 0:
        return("Succeeded.")
    else:
        return("Failed. (Probably no such a room.)")
    conn.close()


# Deroll a student from a course
def delReg(name, course):
    "Deroll a student from a course"
    conn = db.connect("localhost", "ztan", "ztan", "ztan_university")
    cursor = conn.cursor()

    sql = """DELETE FROM Enrolled
        WHERE Enrolled.student IN (SELECT id
        FROM student
        WHERE name = %s) AND course = %s;"""
    cursor.execute(sql, (name, course))
    conn.commit()
    row = cursor.rowcount
    conn.close()
    if row > 0:
        return("Succeeded.")
    else:
        return("Failed. (Probably no such a record.)")


# Enrolled student into a class
def enrollCourse(course, name, cred):
    "Enrolled student into a class."
    conn = db.connect("localhost", "ztan", "ztan", "ztan_university")
    cursor = conn.cursor()

    get_name = """SELECT id
        FROM Student
        WHERE name = %s;"""
    cursor.execute(get_name, name)
    id = cursor.fetchone()
    if id is None:
        conn.close()
        return("Student not found.")
    else:
        enroll = "INSERT INTO Enrolled VALUES (%s, %s, %s);"
        cursor.execute(enroll, (id[0], course, cred))
        conn.commit()
        row = cursor.rowcount
        conn.close()
        if row > 0:
            return("Succeeded.")
        else:
            return("Failed. No rows updated.")
