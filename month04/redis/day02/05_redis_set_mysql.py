import redis
r = redis.Redis(host="localhost",port=6379,db=0)
# songs = {100:"song1",150:"song2",200:"song3",260:"song4"}
songs = {"song1":100,"song2":150,"song3":200,"song4":260}
r.zadd("mysong",songs)
r.zincrby("mysong",300,"song1")
sord_song = r.zrevrange("mysong",0,2,withscores=True)
print(sord_song)
for i in range(1,4):
    print("第{}名:{} 播放次数{}".format(i,sord_song[i-1][0].decode(),
                                  int(sord_song[i-1][1])))

phones = {"huawei":5500,"oppo":4660,"iphone":3580}
r.zadd("phone",phones)
phoneb = r.zrevrange("phone",0,-1)
phone_sord = [phone.decode() for phone in phoneb]
print(phone_sord)





