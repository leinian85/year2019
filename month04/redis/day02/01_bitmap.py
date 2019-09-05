"""位图操作寻找活跃用户"""
import redis

r = redis.Redis(host="leinian",port=6379,db=0)

#user:001 一年中第5天和第200天登录
r.setbit("user:001",4,1)
r.setbit("user:001",199,1)


#user:002 一年中第100天和第300天登录
r.setbit("user:002",99,1)
r.setbit("user:002",299,1)


#user:003 一年中登录了100次以上
for i in range(5,108):
    r.setbit("user:003",i,1)

#user:004 一年中登录了100次以上
for i in range(150):
    r.setbit("user:004",i,1)

# 取出用户的活跃天数
keys = r.keys("user:*")
active = []
noactive = []
for keyb in keys:
    key = keyb.decode()
    count = r.bitcount(key)
    user = (key,count)
    if count > 100:
        active.append(user)
    else:
        noactive.append(user)

print("活跃用户:",active)
print("不活跃用户:",noactive)