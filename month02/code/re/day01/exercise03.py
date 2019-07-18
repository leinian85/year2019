"""
regex2.py
match 对象属性演示
"""
import re
pattern = r"(ab)cd(?P<pig>ef)"
regex = re.compile(pattern)
obj = regex.search("abcdefghi")

#属性变量
print(obj.pos)
print(obj.endpos)
print(obj.re)
print(obj.string)
print(obj.lastgroup) #最后一组的组名
print(obj.lastindex) #最后一组的序列号

