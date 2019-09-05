import redis
r = redis.Redis(host="leinian",port=6379,db=0)

# hset hget
r.hset("user001","name","Lucy")
name = r.hget("user001","name")
print(name) # b'Lucy'

# hmset hmget
user = {
    "name":"Lucy",
    "age":25,
    "gender":"F"
}
r.hmset("user001",user)
user = r.hmget("user001","name","age","gender")
print(user) # [b'Lucy', b'25', b'F']

# hgetall hkeys hvals
user001 = r.hgetall("user001")
print(user001) # {b'name': b'Lucy', b'age': b'25', b'gender': b'F'}

keys = r.hkeys("user001")
print(keys) # [b'name', b'age', b'gender']

vals = r.hvals("user001")
print(vals) # [b'Lucy', b'25', b'F']

# hdel
r.hdel("user001","gender","age")
print(r.hgetall("user001"))


