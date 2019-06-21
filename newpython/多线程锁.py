from threading import Lock
from threading import RLock

b = RLock()
print(b)
b.acquire()
print(b)