list_name = ["张三丰","张翠山","张无忌"]
for i in list_name:
    print(i)

listiter =list_name.__iter__()
while True:
    try:
        item = listiter.__next__()
        print(item)
    except StopIteration:
        break

