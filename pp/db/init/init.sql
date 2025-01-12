CREATE DATABASE IF NOT EXISTS pp;

USE pp;

CREATE TABLE IF NOT EXISTS auth(
   id INT NOT NULL AUTO_INCREMENT,
   username VARCHAR(50) NOT NULL UNIQUE,
   passwd VARCHAR(100) NOT NULL,
   PRIMARY KEY (ID) 
);

CREATE TABLE IF NOT EXISTS users(
    userid VARCHAR(36) NOT NULL,
    fullname VARCHAR(100) NOT NULL,
    username VARCHAR(50) NOT NULL
);

LOAD DATA LOCAL INFILE 'users.csv' INTO TABLE users FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n';