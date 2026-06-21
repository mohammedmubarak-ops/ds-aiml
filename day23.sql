create database Mohammed;
use Mohammed;
show tables;
create table user(name varchar(30));
show tables;
insert into user values("Mohammed");
select * from user;
set SQL_SAFE_UPDATES = 0;
update user set name = "MOHAMMED" where name = "Mohammed" ;
select * from user;
delete from user where name = "MOHAMMED" ;
select * from user ; 
drop table user ;
show tables ;
drop database Mohammed ; 

use dumpdata;
select * from user ;