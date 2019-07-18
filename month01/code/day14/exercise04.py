import double_list_helper as dlh
list01 = [
    ["00", "01", "02", "03"],
    ["10", "11", "12", "13"],
    ["20", "21", "22", "23"],
]
# 在二维列表中，获取13位置，向左，3个元素
re = dlh.DoubleListHelper.get_elements(list01, dlh.Vector2(1, 3), dlh.Vector2.left(), 3)
for item in re:
    print(item)
# 在二维列表中，获取22位置，向上，2个元素
re = dlh.DoubleListHelper.get_elements(list01, dlh.Vector2(2, 2), dlh.Vector2.up(), 2)
for item in re:
    print(item)
# 在二维列表中，获取03位置，向下，2个元素
re = dlh.DoubleListHelper.get_elements(list01, dlh.Vector2(0, 3), dlh.Vector2.down(), 2)
for item in re:
    print(item)