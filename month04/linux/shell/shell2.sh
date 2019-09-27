#!/bin/bash
# ping -c 2 176.215.22.97
for i in {2..254}
do
    ping -c 2 176.215.22.$i &> /dev/null
    if [ $? -eq 0 ];then
    	echo 172.215.22.$i "可用"
    fi
done
