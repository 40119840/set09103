DROP TABLE if EXISTS user;

 CREATE TABLE user (
     idUser integer PRIMARY KEY autoincrement,
     username varchar(50) NOT NULL,
     password varchar(300) NOT NULL,
); 

/*
 CREATE TABLE posts (
    idPost PRIMARY KEY autoincrement,
    idUser integer,
    text varchar(400) NOT NULL,
    FOREIGN KEY (idUser) REFERENCES user(idUser)
 ); 
 /*
