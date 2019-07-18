import re

# # str = "asdf.jpg"
# # str = "How are you?"
str = "How are You? 18"
print(re.findall("[A-Z]*", str))
#
# print(re.findall("\.jpg$",str))
#
# # print(re.findall("ae*",str))
# # print(re.findall("[A-Z][A-Za-z]*",str))
# # print(re.findall("[0-9]+",str))
#
# num = "167  -28  29  -8 1"
# # print(re.findall("-?[0-9]+",num))
# # print(re.findall("-?\d+",num))
#
# str1 = "Port-9 Error 我 #404# %@STD"
# # print(re.findall("[^ ]+",str1))
#
# num1 = "13816013302"
#
# # print(re.findall("1[0-9]{10}",num1))

# \s 匹配任意空字符 \S 匹配任意非空字符
str = "  buib  bh mio"
print(re.findall("\s+", str))

# \A 以...开头 \Z 以...结尾
str = "www.bai.com"
print(re.findall("\Awww.*com\Z", str))

# \b 匹配单词边界 \B 匹配非单词边界  单词(数字字母下划线以及正常的UTF8格式的字符)
str = "This is a test 123 65 num007 "
print(re.findall("\\bis\\b", str))  # 匹配第二个 is
print(re.findall(r"\bis\b", str))  # 匹配第二个 is
print(re.findall(r"\Bis\b", str))  # 匹配第一个 is
print(re.findall(r"\b[0-9]+\b", str))  # 匹配单独是数字的字符 如:123 65

str = "2**10"
print(re.findall("[\*]+", str))

str = "12 -36 415 12.01 2.3"
print(re.findall(r"-?[0-9]+\.?[0-9]*", str))
print(re.findall("-?[0-9]+\.?[0-9]*", str))

str = "日薪:$100"
print(re.findall("\$\d+", str))

# 贪婪模式  和 非贪婪模式(在重复的元字符后面加上?就会匹配最少的次数)
str = "abbbbb"
print(re.findall(r"ab*?", str))

s = "[花千骨],[陆贞传奇],[新还珠格格],[楚乔传]"
print(re.findall(r"\[\w+\]", s))

# 练习:
# 1 匹配.com邮箱格式的字符串
str = "udfewi_342@qq.com"
print(re.findall(r"^[a-z][a-z0-9_]*@[a-z]+.com\Z", str))
print(re.findall(r"\w+@\w+\.com", str))
# 2 匹配一个密码 8- 12 位数字+字母+_构成
str = "dnde_1586_s"
print(re.findall(r"[a-z0-9_]{8,12}", str))
# 3 匹配一个数字 整数,负数,整数,小数,分数1/2,百分数45%
str = "123 -456 12.36 1/2 45% "
print(re.findall(r"-?[\d]+[\./]?[\d]+%?", str))
# 4 匹配一段文字中以大写字母开头的单词,注意单词可能有 iPthon(不算) H-base(算)
str = "iPhone IPhone Hbase H-base H_BNDUI"
print(re.findall(r"\b[A-Z][-_a-zA-Z]*", str))

str = "ababababababab"
print(re.findall(r"(ab)+",str))
print(re.search(r"(ab)+",str))
print(re.search(r"(ab)+",str).group())
print(re.search("(ab)+",str).group(1))
print(re.search("(?P<ab>ab)+",str).group("ab"))

str = "李代桃僵"
str = "王者荣耀"
print(re.findall("[王李]\w{1,3}",str))
print(re.search("(王|李)\w{1,3}",str).group())

str = "42011719590508011X"
print(re.findall("\d{17}[X\d]$",str))


