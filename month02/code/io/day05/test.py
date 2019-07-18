with open("1.txt","rb+") as f:
    print(f.read(2))
    f.write(b"fff")
    print(f.read())
    print(f.tell())


