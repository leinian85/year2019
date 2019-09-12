# class iterablesb
#
# class iterables(a):
#     def __iter__(self):
#         return iterablesb(a)
#
#
lista = [1,2,3,4,5]
list_obj = lista.__iter__()
while True:
    try:
        print(list_obj.__next__())
    except:
        pass