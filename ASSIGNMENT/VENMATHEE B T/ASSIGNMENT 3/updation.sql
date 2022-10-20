CREATE DATABASE IF NOT EXISTS `login1` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `login1`;
CREATE TABLE IF NOT EXISTS `accounts` (
	`id` int(11) NOT NULL AUTO_INCREMENT,
  	`username` varchar(50) NOT NULL,
  	`password` varchar(255) NOT NULL,
  	`email` varchar(100) NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
select * from accounts;
select * from accounts;

INSERT INTO `accounts` (`id`, `username`, `password`, `email`) VALUES (5, 'rithi', 'rithi1', 'rithi@rithi1.com');
INSERT INTO `accounts` (`id`, `username`, `password`, `email`) VALUES (6, 'priya', 'pri1', 'pri@pri1.com');
select * from accounts;
update accounts set password='rithi@15' where id=5;
delete from accounts where id=6;
select * from accounts;