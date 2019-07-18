import re

str = '''Hello 
北京'''
# A 只匹配ASSII编码
print(re.findall(r"\w+", str))
print(re.findall(r"\w+", str, flags=re.A))

# I 不区分大小写
print(re.findall(r"[a-z]+", str))
print(re.findall(r"[a-z]+", str, flags=re.I))

# S 让.可以匹配换行
print(re.findall(r".+", str))
print(re.findall(r".+", str, flags=re.S))

# M 使^,$可以匹配每一行的开头和结尾
print(re.findall(r"^北京", str))
print(re.findall(r"^北京", str, flags=re.M))

# | 既想匹配换行,有想不区分大小写
print(re.findall(r"[a-z]+.+", str, flags=re.I | re.S))
