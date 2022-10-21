--2.perform UPDATE,DELETE queries with the user table

--inserting items in  user table
INSERT INTO `user` (`id`, `username`, `password`,  `rollno`  ,   `email`) VALUES (1, 'venmathee', 'ven31', 'cse001','matheethil@gmail.com');
INSERT INTO `user` (`id`, `username`, `password`, `rollno`, `email`) VALUES (2, 'Durga', 'durga04','cse002', 'durga19cse04@gmail.com');
INSERT INTO `user` (`id`, `username`, `password`, `rollno`, `email`) VALUES (3, 'Priyanka', 'pri19','cse003', 'priyanka@gmail.com');
INSERT INTO `user` (`id`, `username`, `password`, `rollno`, `email`) VALUES (4, 'Rithiha', 'rithi22','cse004', 'rithiha@gmail.com');
select * from user;


--update the user table
update user  set rollno='19cse001' where id=1;


--deleting the user table
delete from user where  email='matheethil@gmail.com';

--viewing the table

select * from user;