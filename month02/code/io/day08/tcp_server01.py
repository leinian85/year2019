import socket
import struct


# def student():
#     try:
#         id = int(input("id:"))
#         name = input("name:")
#         score = float(input("score:"))
#         age = int(input("age:"))
#         return (id, name.encode(), score, age)
#     except ValueError:
#         print("格式错误")
#         return ()


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("127.0.0.1", 18629))
st= struct.Struct("i20sfi")
while True:
    data,adress = s.recvfrom(4096)
    student_info = st.unpack(data)
    print(student_info[0],student_info[1].decode(),student_info[2],student_info[3])
