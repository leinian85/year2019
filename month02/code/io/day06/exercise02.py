with open("1.txt","r+") as f:
    sum = 0
    for item in f.readlines():
        sum += len(item)
        f.seek(sum)
        print(f.tell())
        f.write("$$$\n")