from socket import socket

sockfd = socket()
for port in range(18629, 18640):
    # try:
    print(port)
    sockfd.bind(("127.0.0.1", port))
    sockfd.listen(5)
    clicnfd, adress = sockfd.accept()
    print("开始接收...")
    while True:
        flag = True
        data = clicnfd.recv(1024)
        if not data:
            break
        file = ""
        if flag and data.decode().split("=")[0] == "name":
            file = "new_" + data.decode().split("=")[1]
            flag = False
        with open(file, "rb+") as f:
            f.write(data)
        clicnfd.send("ok".encode())
            # while True:
            #     data = clicnfd.recv(1024)
            #     if not data:
            #         break
            #     filetype = data[0]
            #     data[1].decode()
    # except Exception as e:
    #     print(e)
