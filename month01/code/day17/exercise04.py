list01 = [1,8,12,58,69,5,14,19,18]

# def condition01(item):
#     return item % 2 == 0
#
# def condition02(item):
#     return item < 10
#
# def condition03(item):
#     return 10 < item < 50

def find(list01,condition):
    for item in list01:
        if condition(item):
            yield item

re1 = find(list01,lambda item:item%2==0)
for item in re1:
    print(item)

# re1 = (item for item in list01 if item % 2 == 0)
# for item in re1:
#     print(item)