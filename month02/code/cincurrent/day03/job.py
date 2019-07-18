from multiprocessing import Process
import threading
import time


def fun(flag):
    a = b = c = 0
    for i in range(7000000):
        a += 1
        b += 1
        c += 1
    print("第%d次,a=%d"%(flag+1,a))



t_start = time.time()
for i in range(10):
    fun(i)
t = time.time() - t_start
print(str(t))  #2.89

# t_start = time.time()
# job = []
# for i in range(10):
#     s = Process(target=fun,args=(i,))
#     job.append(s)
#     s.start()
# for i in job:
#     i.join()
# t = time.time() - t_start
# print(str(t))  #0.75

# t_start = time.time()
# job = []
# for i in range(10):
#     s = threading.Thread(target=fun,args=(i,))
#     job.append(s)
#     s.start()
#
# for i in job:
#     i.join()
# t = time.time() - t_start
# print(str(t))  #10