from threading import *
from random import random
from time import *

p = Semaphore(3)


def cash():
    tn = current_thread().getName()
    p.acquire()
    t = random()*5
    print(tn,"开始办理业务")
    sleep(t)
    print(tn,"业务办理完毕")
    p.release()


bt = time()  # 记录开始时间
threads = list()
for i in range(20):
    t = Thread(target=cash)
    t.start()
    threads.append(t)

for t in threads:
    t.join()

et = time()
print("消耗时间:",et-bt)
