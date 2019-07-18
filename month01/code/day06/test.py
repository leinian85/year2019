list1 = [1,2,3,4,5,6]
list2 = [i for i in list1]
# print(list2)
# print(" ".join("%d"%i for i in list2))

dict_a = dict([("张无忌","男"),("赵敏","女")])

dict_person = {"张无忌":{"男","28岁","身高1.80"},
               "赵敏":{"女","26岁","身高1.70"},
               "小昭":{"女","27岁","身高1.60"}}


#方法一：
for key in dict_a:
    print(key)
    print(dict_a[key])

#方法二：
for key in dict_a.keys():
    print(key)
    print(dict_a[key])

#方法三：
for value in dict_a.values():
    print(value)

print("方法四：")
for k,v in dict_a.items():
    print(k)
    print(v)

# dict_b = {(1,2):"12",(2,3):"23"}
# for i in dict_b.items():
#     print(dict_b[i[0]])
