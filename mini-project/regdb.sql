create database regdb;

use regdb;
drop table cust;
create table cust(name varchar(30), passw varchar(20),phone varchar(20) primary key,email varchar(30));
select * from cust;
delete from cust where name='pranav';

create table Pack(pid int(30) primary key,paname varchar(30),days int(10),price int(10));
select * from Pack;
insert into Pack values(1,'GOA',1,8500);
insert into Pack values(2,'RAJASTHAN',1,9000);
insert into Pack values(3,'KERALA', '1','6500');
insert into Pack values(4,'MALAYSIA','1','117000');
insert into Pack values(5,'AUSTRALIA','1','158000');
insert into Pack values(6,'CANADA','1','195000');
insert into Pack values(7,'MANALI','3','85000');
insert into Pack values(8,'JAMMU','4','75000');
insert into Pack values(9,'EGYPT','6','184500');
insert into Pack values(10,'UK','4','145000');
alter table cust add pid int(30);
alter table cust ADD CONSTRAINT idd FOREIGN KEY(pid)
references Pack (pid);
alter table cust ADD primary key(phone);
alter table cust drop pid;
