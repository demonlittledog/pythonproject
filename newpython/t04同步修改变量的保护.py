# 锁
from threading import Thread
from threading import Lock

n = 0
p = Lock()  # 创建锁


def addn():
    global n
    n += 1


def taskrun():
    for k in range(1000000):
        p.acquire()  # 请求🔑
        addn()
        p.release()  # 释放


task1 = Thread(target=taskrun)
task2 = Thread(target=taskrun)
task1.start()
task2.start()
task1.join()
task2.join()
print(n)
