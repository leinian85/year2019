创建数据库:
CREATE DATABASE dict charset=utf8;

#创建表
## 词典表
CREATE TABLE words (
  word varchar(100) DEFAULT NULL,
  exp text
);

## 用户表
create table users(
    user_id int auto_increment primary key,
    name varchar(100),
    password varchar(100)
);

#查询历史明细
create table list_history(
    id int auto_increment primary key,
    user_id int,
    word varchar(100),
    select_time timestamp
);