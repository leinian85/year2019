import socket
import random

for port in range(18629, 18640):
    try:
        print(port)
        socketfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        socketfd.bind(("0", port))

        socketfd.listen(5)

        while True:
            print("wating...")
            clinkfd, adrss = socketfd.accept()
            with open("log", "a+") as f:
                while True:
                    log= adrss[0]
                    data = clinkfd.recv(1024)
                    if not data:
                        break
                    str01 = "hello " + data.decode()
                    log += data.decode()
                    # print(adrss)
                    print(log)
                    # f.write(log)
                    clinkfd.send(str01.encode())
                clinkfd.close()

        socketfd.close()
    except OSError:
        pass
    except socket.error:
        pass
