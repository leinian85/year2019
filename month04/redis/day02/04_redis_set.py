import redis
r = redis.Redis(host="localhost",port=6379,db=0)

r.sadd("myset1","A","B","C","X","Y","Z")
print(r.smembers("myset1"))
print(r.scard("myset1"))
print(r.sismember("myset1","A"))
print(r.sismember("myset1","E"))
r.sadd("myset2","A","B","C","E","F","G")
print(r.sinter("myset1","myset2"))
print(r.sunion("myset1","myset2"))

myset = {item.decode() for item in r.sunion("myset1","myset2")}
print(myset)
