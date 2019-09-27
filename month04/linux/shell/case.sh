#!/bin/bash

read -p "请输入一个字符:" str
if [ $str == 'q' ];then
	exit
elif [ ${#str} -ne 1 ];then
	exit
fi

case $str in
[a-zA-Z])
	echo "字母";;
[0-9])
	echo "数字";;
*)
	echo "其它字母";;
esac

