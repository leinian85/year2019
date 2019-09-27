#!/bin/bash

name="abcdefg"
# 获取字符串的长度
echo "字符串的长度:"${#name}

# 字符串切片
echo "字符串切片:"${name:1:3}
echo "字符串切片:"${name:3}

