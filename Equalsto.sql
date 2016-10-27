# This is the script to create the tables inside the database

DROP DATABASE IF EXISTS equalsto;
CREATE DATABASE IF NOT EXISTS equalsto;
USE equalsto;

DROP TABLE IF EXISTS users ,
                     questions,
                     answers,
CREATE TABLE users (
    UserID      INT       NOT NULL,
    Username    VARCHAR(14)       NOT NULL,
    Firstname   VARCHAR(14)        NOT NULL,
    lastname    VARCHAR(16)        NOT NULL,
    gender      ENUM ('M','F')    NOT NULL,    
    email        VARCHAR(40)      NOT NULL,
    PRIMARY KEY (UserID)
)ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1;


CREATE TABLE questions (
    UserID            INT           NOT NULL,
    question_ID       int            NOT NULL,
    question_String   VARCHAR(40)     NOT NULL,
     answer1          VARCHAR(40)     NOT NULL,
     answer2          VARCHAR(40)     NOT NULL,
     times_answered   INT             NOT NULL,
     answered_yes     ENUM('Y','N')    NOT NULL,   
     PRIMARY KEY (userID), REFERENCES users(userId)
    
)ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1;


CREATE TABLE answers (
 
     UserID           INT            NOT NULL,
   answerSetID       INT             NOT NULL,
    question_ID     INT             NOT NULL,
   answer1      VARCHAR(40)         NOT NULL,
   answer2      VARCHAR(40)         NOT NULL,
   answer3      VARCHAR(40)         NOT NULL,
   answer4      VARCHAR(40)         NOT NULL,
   answer5      VARCHAR(40)         NOT NULL,
   answer6      VARCHAR(40)         NOT NULL,
   answer7      VARCHAR(40)         NOT NULL,
   answer8      VARCHAR(40)         NOT NULL,
   answer9      VARCHAR(40)         NOT NULL,
   answer10     VARCHAR(40)         NOT NULL,
    PRIMARY KEY (UserID), REFERENCES users(userId)
    
)ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1;
 



