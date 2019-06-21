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

# Create tables

cursor.execute("""CREATE TABLE Customer(
id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
name varchar(35) NOT NULL,
add1 varchar(35) NOT NULL,
add2 varchar(35),
add3 varchar(35),
city varchar(35) NOT NULL,
st varchar(35) NOT NULL,
courntry varchar(35) NOT NULL DEFAULT 'US',
postcode varchar(35) NOT NULL,
created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
deact TIMESTAMP,
balanace DECIMAL(6,2),
account_status VARCHAR(10) NOT NULL DEFAULT 'ACTIVE'
)""")

cursor.execute("""CREATE TABLE Sensor(
id INT NOT NULL,
datesample TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
cm varchar(20) NOT NULL,
sensorserial varchar(50) NOT NULL,
sensortype varchar(2) NOT NULL,
sensordata DECIMAL(5,5) NOT NULL
)""")

cursor.execute("""CREATE TABLE Notes(
id INT NOT NULL,
date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
priority varchar(10),
personID int,
Note Tinyblob
)""")

cursor.close()
