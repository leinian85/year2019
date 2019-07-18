'''
    字典推导式
'''
list01 = ["张无忌","赵敏","小昭","周芷若"]
list02 = [101,102,103,104]
dict_all = {item:len(item) for item in list01}
print(dict_all)
dict_all2 = {list01[i]:list02[i] for i in range(0,4)}
print(dict_all2)

dict_all03 = {v:k for k,v in dict_all2.items()}
print(dict_all03)
