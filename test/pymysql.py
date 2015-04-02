#!/usr/bin/python
# -*- coding: utf-8 -*-


print "Content-Type: text/html"
print # a blank line must follow the last HTTP headers

import cgi
import cgitb; cgitb.enable()
import MySQLdb as mdb
import sys

try:
    con = mdb.connect('localhost', 'ztan', 'ztan', 'ztan');

    cur = con.cursor()
    cur.execute("SELECT VERSION()")

    ver = cur.fetchone()
    
    print "Database version : %s " % ver
    print "<br><br>"
    sql = "SELECT * FROM test"
    cur.execute(sql)
    data = cur.fetchall()
    print data
    print "<br><br>"



    
except mdb.Error, e:
  
    print "Error %d: %s" % (e.args[0],e.args[1])
    sys.exit(1)
    
finally:    
        
    if con:    
        con.close()
