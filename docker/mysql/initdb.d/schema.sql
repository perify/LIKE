CREATE TABLE `tweet` (
  `num` int NOT NULL AUTO_INCREMENT,
  `id` varchar(20) DEFAULT NULL,
  `teatime` datetime DEFAULT NULL,
  `tweet` varchar(120) DEFAULT NULL,
  `likec` int DEFAULT '0',
  `retweet` int DEFAULT '0',
  PRIMARY KEY (`num`)
);

CREATE TABLE `users` (
  `ID` varchar(20) NOT NULL,
  `PASSWORD` varchar(60) NOT NULL,
  `EMIL` varchar(30) NOT NULL
);