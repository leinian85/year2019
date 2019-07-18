list01 = [3,5,2,1,7,0,12,11,8]
def double_num1(list_tager):
    listtemp = []
    for item in list_tager:
        if item % 2 == 0 :
            listtemp.append(item)
    return listtemp

def double_num(list01):
    for item in list01:
        if item % 2 ==0:
            yield item

a = double_num(list01)
for i in a:
    print(i)