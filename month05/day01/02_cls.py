import numpy as np

# 第一种设置的dtype的方式
data = [
    ('zs',[80,90,60],20),
    ('ls',[70,80,90],19),
    ('ww',[60,50,50],20)
]

st = np.array(data,dtype="U3,3int32,int32")
print(st)
print(st[1][1])

# 第二种设置的dtype的方式
a = np.array(
    data,dtype=[
        ("name","str",2),
        ("score","int32",3),
        ("age","int32",1)
    ])
print(a)
print(a[2]["score"])

# 第三种设置的dtype的方式
a = np.array(
        data,
        dtype={
            "names":["name","score","age"],
            "formats":["U2","3int32","int32"]
            }
        )
print(a)

print(a[1]["score"])