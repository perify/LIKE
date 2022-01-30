CREATE TABLE tweet (
  num int NOT NULL AUTO_INCREMENT,
  username varchar(20) DEFAULT NULL,
  tweet_time datetime DEFAULT NULL,
  tweet varchar(120) DEFAULT NULL,
  PRIMARY KEY (num)
);

CREATE TABLE users (
  num int NOT NULL AUTO_INCREMENT,
  username varchar(20) UNIQUE NOT NULL,
  password varchar(60) NOT NULL,
  email varchar(30) UNIQUE NOT NULL,
  primary key (num)
);

CREATE TABLE likes (
    tweet_number int NOT NULL,
    user_number int NOT NULL,
    like_time datetime DEFAULT NULL,
    primary key (tweet_number, user_number),
    unique (tweet_number, user_number)
);