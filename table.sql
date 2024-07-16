CREATE TABLE `bandwidth` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Server_ID` int(11) DEFAULT NULL,
  `Sponsor` varchar(255) DEFAULT NULL,
  `Server_Name` varchar(255) DEFAULT NULL,
  `Timestamp` datetime DEFAULT NULL,
  `Distance` float DEFAULT NULL,
  `Ping` float DEFAULT NULL,
  `Download` float DEFAULT NULL,
  `Upload` float DEFAULT NULL,
  `Share` varchar(255) DEFAULT NULL,
  `IP_Address` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
)