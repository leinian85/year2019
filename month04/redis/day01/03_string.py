import redis

r = redis.Redis(host="localhost", port=6379, db=0)

# 操作string
r.set("user001:name","guods")
print(r.get("user001:name"))
m_dict = {
    "user001:age":"20",
    "user001:gender":"M",
}
r.mset(m_dict)
print(r.mget("user001:name","user001:age","user001:gender"))

print(r.strlen("user001:name"))
# 操作数值类型

r.incrby("user001:age",2)
print(r.get("user001:age"))
r.incr("user001:age",2)
print(r.get("user001:age"))

r.decrby("user001:age")
print(r.get("user001:age"))

r.incrbyfloat("user001:age",0.5)
print(r.get("user001:age"))
r.incrbyfloat("user001:age",-1.5)
print(r.get("user001:age"))
