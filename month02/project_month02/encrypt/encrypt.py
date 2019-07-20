import hashlib

SALT = "#&Aid_"  # 盐


# 加密
def encrypt(name, pwd):
    hash = hashlib.md5((name + SALT).encode())
    hash.update(pwd.encode())
    password = hash.hexdigest()
    return password


pwd = encrypt("leinian", "123456")
print(pwd)
print(len("70ce9d243f81abffb79fba6241c76c58"))
