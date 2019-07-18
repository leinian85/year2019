"""
regex.py re模块功能函数演示
"""
import re

str = "Alex:1994,Sunny:1996"

pattern = r"(\w+):\d+"
l = re.findall(pattern, str)
print(l)

# compile
pattern = r"\w+:\d+"
regex = re.compile(pattern)
l = regex.findall(str)
print(l)
l = regex.findall(str, 10)
print(l)

# 替换目标字符串
"""
regex1.py re模块 功能演示函数
生成 match对象的函数
"""
str = "今年是2019年,见过70周年"
# 完全匹配
m = re.fullmatch(r"[,\w]+", str)
print(m.group())

#匹配开始位置
m = re.match(r"\w+?",str)
print(m.group())

#匹配第一处符合正则规则的内容
m = re.search(r"\d+",str)
print(m.group())