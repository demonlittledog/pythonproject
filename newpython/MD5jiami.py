import hashlib
#创建一个MD5对象
m = hashlib.md5()
#创建一个对象
s = "123456".encode()
print(s)
#调用update方法进行加密
m.update(s)
r = m.digest()
print(r)
print(m)
h = m.hexdigest()
print(h)


#nt 系统
import os
print(os.name)

s = 0
print(s)

#time函数
from time import time
print(time())
t = time()
print(t)
print(t/60/60/24/365.2422)

import datetime as dt
d1 = dt.datetime.now()
print(d1.today())
tt = dt.timedelta(hours=100000)
print(d1-tt)

tt = dt.timedelta(days=10000)
print(d1+tt)

#范围多大乘以多少，然后偏移量有多大再加多大
#100~103   random*3 + 100
import random as rnd
print((rnd.random())*3 +100)

a = [100,27.2,33,-6,95]
c=map(lambda x: x-(-6),a)
print(rnd.randint(1,100))

a = [1,2,1,2,1,2,1,2,0,0,0,0]
rnd.shuffle(a)
print(rnd.choice(a))
print(rnd.choices(a))









