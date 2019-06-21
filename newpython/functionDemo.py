#参数
def functiondemo():
    pass

#位置参数（必须参数）
def f1(x,y):
    print("参数x值为:", x)
    print("参数y值为:", y)


f1(19, 5)

#参数的默认值（默认参数，可选参数）
def f2(x, y, z=17):
    print("参数x值为:", x)
    print("参数y值为:", y)
    print("参数z值为:", z)


f2(7, 8)

#多个具有默认值的参数
def f3(x, y=6, z=17):
    print("参数x值为:", x)
    print("参数y值为:", y)
    print("参数z值为:", z)

#命名参数
f3(7, z=19)

#收集参数，收集位置参数
def f4(*para):
    print(para)
    print(type(para))

#命名参数
f4(3, 5, 9)

def my_sum(*x):
    s=0
    for v in x:
        s += v
    return s

q = my_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print(q)

#收集命名参数
def f5(**x):
    print(x)
    print(type(x))
    for k in x:
        print(k, "=", x.get(k))

#任意参数收集
def f6(*y, **x):
    for i in y:
        print(i)
    for k in x:
        print(k, "=", x.get(k))

# #使用元祖和字段提供收集参数，*和**的使用
# a=(3,6,9)
# b={"v1":111,"v2":222}
# f6(*a, **b)
#
# def g(x):
#     for i in range(x):
#         print("生成", i)
#         yield i
#
# t = g(9)
# for x in t:
#     d = x
# print(d)


def run(f,*x,**y):
    import time
    bt = time.time()
    f(*x, **y)
    et = time.time()
    print("消耗时间：", et-bt)

u = f6
run(u, 3, 6)

from time import time

#函数装饰器
def cost_time(a_func):
    from time import time

    def inner(*a, **b):
        bt = time()
        k =a_func(*a, **b)
        et = time()
        print("耗时",et-bt)
        return k
    return inner

@cost_time
def rnd_cost(m):
    print("rnd_cost 开始 with", m)
    from random import random
    x = random()
    from time import sleep
    sleep(x*5)
    print("rnd_cost 结束")

t = rnd_cost("think")
print(t)