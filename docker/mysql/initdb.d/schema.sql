CREATE TABLE `tweet` (
  `num` int NOT NULL AUTO_INCREMENT,
  `username` varchar(20) DEFAULT NULL,
  `teatime` datetime DEFAULT NULL,
  `tweet` varchar(120) DEFAULT NULL,
  `like_count` int DEFAULT '0',
  `retweet` int DEFAULT '0',
  PRIMARY KEY (`num`)
);

CREATE TABLE `users` (
  `username` varchar(20) UNIQUE NOT NULL AUTO_INCREMENT,
  `password` varchar(60) NOT NULL,
  `email` varchar(30) UNIQUE NOT NULL,
  primary key (`username`)
);