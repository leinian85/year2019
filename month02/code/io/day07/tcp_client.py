from socket import *
scokfd = socket()
scokfd.connect(("127.0.0.1",18629))
while True:
    str01 = input(">>")
    if str01 == "":
        break
    scokfd.send(str01.encode())
    data = scokfd.recv(1024)
    print(data.decode())
scokfd.close()