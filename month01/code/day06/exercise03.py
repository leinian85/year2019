str_temp = input("请输入日期:")
days = (31,28,31,30,31,30,31,31,30,31,30,31)
month = 1
a = 0
day = 1
total_days = 0
for i in range(0,len(str_temp)):
    if str_temp[i] == "月":
        month = str_temp[0:i]
        a = i+1
    elif str_temp[i] == "日":
        day = str_temp[a:i]
print("%s月%s日"%(month,day))

for i in range(0,int(month) -1):
    total_days += days[i]

print(total_days+int(day))
