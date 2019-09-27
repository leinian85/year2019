#!/bin/bash
i=1
while [ $i -le 5 ]
do
    echo $i
    let i++
done
# 生成10以内的随机数
echo "生成10以内的随机数"
for i in {1..10}
do
    echo $[RANDOM%10]
done
