import redis
import time
import random
from multiprocessing import Process


class Spider:
    def __init__(self):
        self.r = redis.Redis(host="localhost", db=0, port=6379)

    # 生产者 - 进程事件函数
    def product(self):
        for page in range(67):
            url = "http://app.mi.com/category/2#page={}".format(page)
            self.r.lpush("xiaomi:app",url)
            time.sleep(random.randint(1,2))

    # 消费者 - 进程事件函数
    def consumer(self):
        while True:
            url = self.r.blpop("xiaomi:app",random.randint(3,5))

            if url:
                print("正在抓取:{}".format(url[1].decode()))
            else:
                print("抓取结束!")
                break
    # 主函数
    def run(self):
        p1 = Process(target= self.product)
        p2 = Process(target= self.consumer)
        p1.start()
        p2.start()
        p1.join()
        p2.join()

if __name__ == "__main__":
    spider = Spider()
    spider.run()