from threading import *
from time import sleep
v = Lock()


def taskrun():
    tn = current_thread().getName()
    while True:
        v.acquire()  # 请求锁
        s = input(tn)
        print(tn,'获取了数据:',s)
        v.release()
        sleep(1)


task1 = Thread(target=taskrun)
task2 = Thread(target=taskrun)
task1.start()
task2.start()
