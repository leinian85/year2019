#!/bin/bash

name="张三丰"
echo "名字为:$name"
echo '名字为:$name'
echo "环境变量USER:$USER"
echo "环境变量PATH:$PATH"
echo "环境变量PWD:$PWD"
echo "环境变量UID:$UID"
echo "位置变量:$1"
echo "位置变量:$2"
mysql -uroo1 -p11111
echo $?
echo $1+$2=`expr $1 + $2` 
read -p "请输入姓名:" name
read -t 3 -p "请输入成绩:" score
echo $name"的成绩是:"$score
let score++
echo $name"的成绩是:"$score

if [ $USER == $name ];then
    echo "YES"
else
    echo "NO"
fi

c=$RANDOM

read -p "请输入数字:" num
if [ $num -gt $c ]; then
    echo "大"
elif [ $num -lt $c  ];then
    echo "小"
else
    echo "对"
fi

echo $c

for i in `seq 5`
do
    echo $i
done
