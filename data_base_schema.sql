
CREATE DATABASE match;

CREATE TABLE students (
    
    sId INT NOT NULL, 
    fisrtName varchar,
    lastNamr varchar,
    email varchar,
    PRIMARY KEY(sId)
    );

CREATE TABLE tutor (
    tId INT NOT NULL,
    fisrtName varchar,
    lastNamr varchar,
    email varchar,
    area_of_stdy varchar,
    
    PRIMARY KEY (Tid)
    );
    
CREATE TABLE instructor (
    Id INT NOT NULL,
    fisrtName varchar,
    lastNamr varchar,
    email varchar,
    area_of_stdy varchar,
    
    PRIMARY KEY (Id)
    );
    
CREATE TABLE course (
    cId INT NOT NULL AUTOINCREMENT, 
    tId INT NOT NULL,
    Id INT  NOT NULL,
    cTitle varchar,
    
    PRIMARY KEY (cId),
    FOREIGN KEY (tId) REFERENCES tutor(tId),
    FOREIGN KEY (Id) REFERENCES instructor(tId) 
    );


CREATE TABLE match (
    mId INT NOT NULL AUTOINCREMENT, 
    sId INT NOT NULL, 
    tId INT NOT NULL,
    PRIMARY KEY(mId),
    FOREIGN KEY (sId) REFERENCES students(sId),
    FOREIGN KEY (tId) REFERENCES tutor(tId)
    );

CREATE TABLE preference (
    pId INT NOT NULL AUTOINCREMENT, 
    preference_1 varchar, 
    preference_2 varchar,
    PRIMARY KEY (pId)
    );
    
CREATE TABLE tutor_courses (
    Id INT NOT NULL AUTOINCREMENT, 
    tId INT,
    cId INT,
    PRIMARY KEY (Id),
    FOREIGN KEY (tId) REFERENCES tutor(tId),
    FOREIGN KEY (cId) REFERENCES course(sId),
);


CREATE TABLE room (
    rId INT NOT NULL AUTOINCREMENT,
    rName varchar,
    PRIMARY KEY (rId)
    );
    
    

CREATE TABLE view_room (
    Id INT NOT NULL AUTOINCREMENT , 
    rId INT NOT NULL,
    cId INT NOT NULL,
    PRIMARY KEY (Id),
    FOREIGN KEY (rId) REFERENCES room(rId),
    FOREIGN KEY (cId) REFERENCES course(cId)
    
    );


CREATE TABLE date (
    dId INT NOT NULL AUTOINCREMENT ,
    curr_date date,
    PRIMARY KEY (dId)
    );
    
CREATE TABLE time (
    Id INT NOT NULL AUTOINCREMENT , 
    curr_time INT,
    PRIMARY KEY (Id)
    );
    
    
CREATE TABLE s_time ( 
    Id INT NOT NULL AUTOINCREMENT , 
    sId INT NOT NULL, 
    dId INT NOT NULL, 
    Id INT NOT NULL,
    PRIMARY HEY(Id),
    FOREIGN KEY (sId) REFERENCES students(sId),
    FOREIGN KEY (dId) REFERENCES date(dId),
    FOREIGN KEY (tId) REFERENCES time(Id),
);


CREATE TABLE tutor_time(
    t_Id INT NOT NULL AUTOINCREMENT,
    tId INT NOT NULL,
    dId INT NOT NULL,
    Id INT NOT NULL,
    PRIMARY KEY(t_Id),
    FOREIGN KEY (tId) REFERENCES tutor(tId),
    FOREIGN KEY (dId) REFERENCES date(dId),
    FOREIGN KEY (tId) REFERENCES time(Id)
    );