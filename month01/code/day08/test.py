
def move(list01,list02,list03):
    list04 = [list01,list02,list03]
    flag = False
    for i in range(len(list04)):
        if bool(list04[i]):
            num01 = [n for n in range(0,3)]
            num01.remove(i)
            for j in num01:
                temp = list04[i][-1]
                if not bool(list04[j]) or list04[j][-1] > temp:
                    list04[j].append(temp)
                    list04[i].pop()
                    flag = True
                    break
            if flag:
                break



a = [3,2,1]
b = []
c = []
for i in range(3):
    move(a,b,c)
print(a)
print(b)
print(c)

# temp = a.pop()
# if not bool(b) or b[-1] > temp:
#     b.append(temp)
# else:

a = [3,2,1];a=[3,2];a=[3]; a=[3]  ; a = []   ;a = [1];a = [1]  ;a=[]
b = []     ;b=[1]  ;b=[1]; b=[]   ; b = [3]  ;b = [3];b = [3,2];b=[3,2,1]
c = []     ;c=[]   ;c=[2]; c=[2,1]; c = [2,1];c = [2];c = []   ;c=[]

a = [4,3,2,1]
b = []
c = []
#空的直接放
a = [4,3,2]
b = [1]
c = []

a = [4,3]
b = [1]
c = [2]

a = [4,3]
b = []
c = [2,1]

a = [4]
b = [3]
c = [2,1]

a = [4,1]
b = [3]
c = [2]

a = [1]
b = [3,2]
c = []

a = []
b = [3,2,1]
c = []