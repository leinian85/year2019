'''
    字典
    1.查找
    2.修改
    3.增加
    4.删除
    5.遍历
'''
dict01 = {}
while True:
    name = input("商品名称：")
    if name == "":
        break
    str_price = input("单价：")
    if str_price == "":
        break
    price = float(str_price)
    dict01[name] = price

for k, v in dict01.items():
    print("%s的单价为：%.2f元" % (k, v))

# for key in dict01:
#     print("%s的单价为：%.2f元" % (key, dict01[key]))
