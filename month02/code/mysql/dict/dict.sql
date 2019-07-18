1.创建数据库: dict (utf8)
2.创建单词表: words 将单词和单词解释分别存入不同的字段
3.将单词存入 words 单词表

create database dict charset = utf8;
create table words(
word varchar(100),
exp text
);