list01 = ("铁扇公主","白雪公主","铁锤公主")

listiter = list01.__iter__()
while True:
    try:
        item = listiter.__next__()
        print(item)
    except StopIteration:
        break

dict01 = {101:"铁扇公主", 102:"白雪公主", 103:"铁锤公主"}
dictiter = dict01.__iter__()
while True:
    try:
        item = dictiter.__next__()
        print(item,dict01[item])
    except StopIteration:
        break