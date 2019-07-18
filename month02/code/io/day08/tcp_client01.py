import socket
import struct

def student():
    try:
        id = int(input("id:"))
        name = input("name:")
        score = float(input("score:"))
        age = int(input("age:"))
        return (id,name.encode(),score,age)
    except ValueError:
        print("格式错误")
        return ()


s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
st = struct.Struct("i20sfi")
while True:
    id = int(input("id:"))
    name = input("name:")
    score = float(input("score:"))
    age = int(input("age:"))
    data = st.pack(id,name.encode(),score,age)
    s.sendto(data,("127.0.0.1", 18629))

