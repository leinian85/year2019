list01 = [1,5,10,2,82,2,10]
str_flag = "N"
for i in range(len(list01)-1):
    for j in range(i+1,len(list01)):
        if list01[i] == list01[j]:
            print("存在相同的")
            print("%d,%d"%(list01[i],list01[j]))
            break
    if str_flag == "Y":
        break