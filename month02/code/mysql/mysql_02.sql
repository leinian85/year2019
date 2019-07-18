create table marathon(
    id int auto_increment primary key,
    name varchar(32),
    enter_time datetime,
    croce time
);

insert into marathon(name,enter_time,croce)
values('赵四','2019-5-18 12:00:00','2:30:30');