# 模拟一个耗时的操作: 文件下载
import time


def downFile(fn, secs):
    '''
    模拟耗时下载一个文件
    :param fn: 文件名
    :param secs: 消耗的时间(秒)
    :return: None
    '''
    i = 0
    while i < secs:
        time.sleep(1)
        i += 1
        print("正在下载:%s[%d/%d]"%(
            fn,i,secs
        ))
    print("下载完成:%s"%fn)


print("顺序执行:")
downFile("a.mp3", 7)
downFile("b.mp3", 12)

# 以上两个耗时的操作顺序执行完,需要19秒
# 如果可以同时进行,则耗时只需要 12秒


# 创建线程
import threading
task1 = threading.Thread(
    target=downFile,  # 线程执行的函数
    args=("a.mp3", 7)  # 函数的参数
)
task2 = threading.Thread(target=downFile,args=("b.mp3", 12))
print("并发执行:")
task1.start()  # 启动线程
task2.start()

task2.join()
print("task2执行完毕")

task1.join()  # 当前线程阻塞到该线程结束
print("tas1执行完毕")

print("执行结束")
