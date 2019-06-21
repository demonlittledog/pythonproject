import threading
import time


def runtask():
    tn = threading.currentThread().getName()
    while True:
        print(tn,"正在运行")
        time.sleep(3)


task1 = threading.Thread(target=runtask)
task1.setDaemon(True)  # 设置守护
task1.start()
task1.join()
print("程序结束")
