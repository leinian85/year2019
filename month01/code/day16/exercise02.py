class GraphIterator:
    def __init__(self, tager):
        self.__tager = tager
        self.__index = 0

    def __next__(self):
        if self.__index > len(self.__tager) - 1:
            raise StopIteration
        item = self.__tager[self.__index]
        self.__index += 1
        return item


class GraphManager:
    def __init__(self):
        self.__list_grap = []

    def set_list_grap(self, value):
        self.__list_grap.append(value)

    def __iter__(self):
        return GraphIterator(self.__list_grap)


gm = GraphManager()
gm.set_list_grap("三角形")
gm.set_list_grap("圆形")
gm.set_list_grap("正方形")

for graph in gm:
    print(graph)

gm1 = gm.__iter__()
while True:
    try:
        item = gm1.__next__()
        print(item)
    except StopIteration:
        break