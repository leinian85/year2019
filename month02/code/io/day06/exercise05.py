with open("1.txt","r+") as f:
    print(f.tell())
    print(f.readline().encode())
    f.seek(-2)
    f.write("$$$")