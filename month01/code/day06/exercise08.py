dict_info = {}
while True:
    name = input("姓名：")
    if name == "":
        break
    fancys = []
    while True:
        fancy = input("请输入喜好：")
        if fancy == "":
            break
        fancys.append(fancy)
    dict_info[name] = fancys

for k,v in dict_info.items():
    print("%s的喜好是：%s"%(k,",".join(v)))