import threading

n = 0


def addn():
    global n
    n += 1


def taskrun():
    for k in range(1000000):
        addn()


task1 = threading.Thread(target=taskrun)
task1.start()
task2 = threading.Thread(target=taskrun)
task2.start()

task1.join()
task2.join()
print(n)
