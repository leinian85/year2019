meaasge = input("请输入字符串：")
set01 = set(meaasge)
list01 = list(set01)
print("".join(list01))

set_manage = {"曹操","刘备","孙权"}
set_technic = {"曹操","刘备","关羽","张飞"}
print("是经理也是技术的：%s" %(" ".join(list(set_manage & set_technic))))
print("是经理不是技术的：%s" %(" ".join(list(set_manage - set_technic))))
print("是技术不是经理的：%s" %(" ".join(list(set_technic - set_manage))))
print("张飞是经理吗：%s"%str({"张飞"} < set_manage))
print("身兼一职的：%s" %(" ".join(list(set_technic ^ set_manage))))
set01 = set_manage
for item in set_technic:
    set01.add(item)
print("经理和技术的有多少人：%d"%len(set01))
print("经理和技术的有多少人：%d"%len(set_technic | set_manage))