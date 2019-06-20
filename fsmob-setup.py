import MySQLdb
import mysql.connector
# set up the login Need to figure out a crypto bag system for security.
fsmob = MySQLdb.connect(host = 'localhost', 
                       user = 'root', 
                       passwd = 'password')
cursor = fsmob.cursor()

#This is a distructive process, we delete everything first.
cursor.execute("DROP DATABASE IF EXISTS fsmob")
cursor.execute("DROP USER IF EXISTS 'fsmob'@'localhost'")

statement = """CREATE USER 'fsmob'@'localhost' IDENTIFIED BY 'password'"""
cursor.execute(statement)
cursor.execute("CREATE DATABASE fsmob")
cursor.execute("GRANT ALL PRIVILEGES ON fsmob.* TO 'fsmob'@'localhost'")
cursor.execute("FLUSH PRIVILEGES")
cursor.execute("USE fsmob")
cursor.execute("""CREATE TABLE Customer(
id varchar(20) PRIMARY KEY NOT NULL,
name varchar(35) NOT NULL,
add1 varchar(35) NOT NULL,
add2 varchar(35),
add3 varchar(35),
city varchar(35) NOT NULL,
st varchar(35) NOT NULL,
courntry varchar(35) NOT NULL DEFAULT 'US',
postcode varchar(35) NOT NULL
)""")
cursor.close()
