import socket
from interpret import Interpret

sockudp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
address = ("127.0.0.1", 18629)
sockudp.bind(address)
inter = Interpret()
while True:
    data, addr = sockudp.recvfrom(1024)
    print(data.decode(), addr)
    interpret = inter.get_interpret(data.decode().strip())
    sockudp.sendto(interpret.encode(), addr)
    with open("log", "a") as f:
        f.write(data.decode() + " " + " ".join("%s" % item for item in addr) + "\n")
        f.write(interpret+"\n")
        f.flush()

sockudp.close()
