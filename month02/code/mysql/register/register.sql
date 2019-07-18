create table users(
    id int auto_increment primary key,
    name varchar(32) not null,
    password varchar(100) not null
);