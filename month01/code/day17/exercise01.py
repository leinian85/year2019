"""
    enumerate
"""


def my_enumerate(iterable_taget):
    index = 0
    for item in iterable_taget:
        yield (index, item)
        index += 1


list01 = [5, 4, 8, 6]
for item in my_enumerate(list01):
    print(item)

list02 = ["孙悟空", "猪八戒", "唐僧", "沙僧"]
list03 = [0, 1, 2, 3]


def my_zip(list01, list02):
    for i in range(0, len(list01)):
        yield (list01[i], list02[i])


for item in my_zip(list03, list02):
    print(item)


re  = (item for item in list03)
print(re)
re1  = [item for item in list03]
print(re1)


