'''
    *#*#*#
    *#*#*#
    *#*#*#
    *#*#*#
'''
for i in range(4):
    for j in range(6):
        if j % 2 == 0:
            print("*", end="")
        else:
            print("#", end="")
    print("")

'''
*
**
***
****
'''
for r in range(4):
    print("*"*(r+1))

for r in range(4):
    for c in range(0,r+1):
        print("*",end=" ")
    print("")