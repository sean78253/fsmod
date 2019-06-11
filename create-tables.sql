CREATE TABLE identity (
cno VARCHAR(20) PRIMARY KEY,
api_key VARCHAR(20) NOT NULL,
mod_date TIMESTAMP
) ;

CREATE TABLE customer (
cno VARCHAR(20) PRIMARY KEY,
cname VARCHAR(50),
consolidatedbill VARCHAR(20),
address1 VARCHAR(50),
address2 VARCHAR(50),
address3 VARCHAR(50),
st VARCHAR(10),
postcode VARCHAR(15),
phone1 VARCHAR(20),
phone2 VARCHAR(20),
contact1 VARCHAR(20),
contact2 VARCHAR(20),
NotesDB VARCHAR(20),
reg_date TIMESTAMP
) ;
