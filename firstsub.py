#! /usr/bin/python
import os, sys 
from crontab import CronTab

path = raw_input("Enter absolute path:\n")



# Now change the directory
os.chdir( path )



fo = open("one.py","w+")
fo.write("#!/usr/bin/python\n")
fo.write("import sys\n")
fo.write("import sqlite3 as lite\n")
fo.write("import time\n")
fo.write("con = lite.connect('test.db')\n")
fo.write("with con:\n")
fo.write("    cur = con.cursor() \n")
fo.write("    cur.execute(\"DROP TABLE IF EXISTS zxcv;\")\n")
fo.write("    cur.execute(\"CREATE TABLE zxcv(tyme TIME);\")\n")
fo.close()

fo = open("two.py","w+")
fo.write("#!/usr/bin/python\n")
fo.write("import sys\n")
fo.write("import sqlite3 as lite\n")
fo.write("import time\n")
fo.write("con = lite.connect('test.db')\n")
fo.write("with con:\n")
fo.write("    cur = con.cursor() \n")
fo.write("    cur.execute(\"INSERT INTO zxcv VALUES( time());\")\n")
fo.write("    cur.execute(\"SELECT * FROM zxcv\")\n")
fo.write("    rows = cur.fetchall()\n")
fo.write("    for row in rows:\n")
fo.write("        print row\n")
fo.write("\n")
fo.close()
path1 = path + "/one.py"
path2 = path + "/two.py"
os.chmod(path1,0777)
os.chmod(path2,0777)

os.system('python one.py')

cron   = CronTab()
croncommand = "python " +path2
job  = cron.new(command= croncommand)
job.minute.every(10)

