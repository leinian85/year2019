a = [1,2]
b = [1,2]
print(id(a),id(b))
print(a is b)
print(a == b)

list01 = [1,2,3,4,5]
print("".join("%d"%item for item in list01))