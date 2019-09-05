import redis

# 创建链接对象
r = redis.Redis(host="localhost",db=0,port=6379)

# 通用命令
key_list = r.keys("*")
print([key.decode() for key in key_list])

print(r.type("mylist"))

print(r.exists("mylist"))

r.expire("mylist",5)

r.delete("mysql")

# list
r.lpush("hero","zhangwuji","zhangsanfeng","zhangcuishan")
r.rpush("hero","zhaomin")
r.linsert("hero","after","zhangcuishan","xiexun")
print(r.llen("hero"))
print(r.lpop("hero")) # b'zhangcuishan'
print(r.rpop("hero")) # b'zhaomin'
r.ltrim("hero",0,2)
print(r.lrange("hero",0,-1))

while True:
    result = r.brpop("hero",3)
    print(result) # (b'hero', b'zhangsanfeng1')
    if not result:
        break
        