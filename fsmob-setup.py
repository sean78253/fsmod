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

cursor.execute("""CREATE USER 'fsmob'@'localhost' IDENTIFIED BY 'password'""")
cursor.execute("CREATE DATABASE fsmob")
cursor.execute("GRANT ALL PRIVILEGES ON fsmob.* TO 'fsmob'@'localhost'")
cursor.execute("FLUSH PRIVILEGES")
cursor.execute("USE fsmob")

# Create tables

cursor.execute("""CREATE TABLE Customer(
Customer_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
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
account_status VARCHAR(10) NOT NULL DEFAULT 'ACTIVE') ENGINE=INNODB
""")

cursor.execute("""CREATE TABLE ClusterMonitor(
Customer_id INT NOT NULL,
INDEX Cluster_Customer_ind (Customer_id),
FOREIGN KEY (Customer_id) REFERENCES Customer(Customer_id) ON DELETE CASCADE,
Cluster varchar(17) NOT NULL,
common_name varchar(20) NOT NULL,
date_added TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
last_seen TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
INDEX Cluster_Seen_ind (Customer_id, Cluster, date_added)) ENGINE=INNODB
""")

cursor.execute("""CREATE TABLE Sensor(
Customer_id INT NOT NULL,
INDEX CustomerSensor_ind (Customer_id), 
FOREIGN KEY (Customer_id) REFERENCES Customer(Customer_id) ON DELETE CASCADE, 
datesample TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
cm varchar(17) NOT NULL,
sensorserial varchar(50) NOT NULL,
sensortype varchar(2) NOT NULL,
sensordata DECIMAL(5,5) NOT NULL) ENGINE=INNODB
""")

cursor.execute("""CREATE TABLE Notes(
Customer_id INT NOT NULL,
INDEX CustomerNotes_ind (Customer_id),
FOREIGN KEY (Customer_id) REFERENCES Customer(Customer_id) ON DELETE CASCADE,
Person_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
priority varchar(10),
Note Tinyblob,
INDEX Notes_idx (Customer_id, Person_id)) ENGINE=INNODB
""")

cursor.execute(""" ALTER TABLE Customer AUTO_INCREMENT=100 """)
cursor.execute(""" ALTER TABLE Notes AUTO_INCREMENT=100 """)

cursor.close()

