# day06 作业
# 1. 三合一
# 2. 当天练习独立完成
# 3. 将1970年到2050年中的闰年，存入列表．
list_year = []
for year in range(1970,2051):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        list_year.append(year)
print(list_year)

# 4. 存储全国各个城市的景区与美食(不用录入),在控制台中显示出来.
#   　北京：
#         景区：故宫,天安门,天坛.
#         美食: 烤鸭,炸酱面,豆汁,卤煮.
#     四川:
#         景区：九寨沟,峨眉山,春熙路．
#         美食: 火锅,串串香,兔头.
dict_feature = {
    "北京":
        {"景区":["故宫","天安门","天坛"],
         "美食":["烤鸭","炸酱面","豆汁","卤煮"]
         },
    "四川":
        {"景区":["九寨沟","峨眉山","春熙路"],
         "美食":["火锅","串串香","兔头"]
         }
}

for k,v in dict_feature.items():
    print("%s:"%k)
    for k1,v1 in v.items():
        print("    %s:%s"%(k1," ".join(v1)))

list_all = []
for item in dict_feature.keys():
    print(item,end="")
    print(dict_feature[item]["景区"])
    for item2 in dict_feature[item]["景区"]:
        list_all.append(item2)
print(list_all)
# 5.(扩展)计算一个字符串中的字符以及出现的次数.
# # 思想：
# # 逐一判断字符出现的次数.
# # 如果统计过则增加１，如果没统计过则等于１.
#
# abcdefce
# a 1
# b 1
# c 2
# d 1
# e 2
# f 1
meassge = "abcdefce"
dict_str = {}
for i in meassge:
    if i not in dict_str.keys():
        dict_str[i] = 1
    else:
        dict_str[i] += 1
for k,v in dict_str.items():
    print("字母%s出现%d次"%(k,v))


# 6.阅读python入门到实践第６章
#
#
#
#
#
#
#
#
#
#
#
#
#
#
