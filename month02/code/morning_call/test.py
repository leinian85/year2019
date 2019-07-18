# if __name__ == "__main__":
#     with open("config","w") as f:
#         for i in range(1,27):
#             f.write("%d %s\n"%(i,chr(64+i)))
#
#     with open("config","r") as f:
#         dict_map = {}
#         for line in f:
#             str_line = line.split(" ")
#             dict_map[int(str_line[0])] = str_line[1].strip()
#
#     print(dict_map)
#

class A:
    pass

class B:
    pass

b = B()

print(isinstance(b,B))
