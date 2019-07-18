message = "How are you"
list_tmp = message.split(" ")
list_tmp2 = []
for i in range(len(list_tmp)-1,-1,-1):
    list_tmp2.append(list_tmp[i])
print(" ".join(list_tmp2))