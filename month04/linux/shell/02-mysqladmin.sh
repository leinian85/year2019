#!/bin/bash

user="root"
passwd="123456"

while :
do		
	count=`mysqladmin -u$user -p$passwd status|awk '{print $4}'`
	echo "`date +%F" "%H:%M:%S` 并发连接数为: $count"
	sleep 2
done
