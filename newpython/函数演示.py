

# 参数
def fnopara():
    pass


def f(x):
    print("参数x值为:", x)


# 位置参数(必要参数)
def f1(x, y):
    print("参数x值为:", x)
    print("参数y值为:", y)


# 参数的默认值(默认参数,可选参数)
def f2(x, y, z=17):
    print("参数x值为:", x)
    print("参数y值为:", y)
    print("参数z值为:", z)


# 多个具有默认值的参数
def f3(x, y=9, z=17, k=0):
    print("参数x值为:", x)
    print("参数y值为:", y)
    print("参数z值为:", z)
    print("参数k值为:", k)


# 收集参数1:位置参数
def f4(*para):
    print(para)
    print(type(para))


def my_sum(*x):
    s = object()
    for v in x:
        s += v
    return s


# 收集参数 2:收集命名参数
def f5(**x):
    print(x)
    print(type(x))
    for k in x:
        print(k, '=', x.get(k))


# 任意参数收集
def f6(*a, **b):
    print("位置参数:")
    for v in a:
        print(v)
    print("命名参数:")
    for k in b:
        print(k, '=', b.get(k))

# 使用元组和字典提供收集参数, *和**的使用
# a = (3,9,2)
# b = {"v1":288,"v2":977}
# f6(*a,**b)


def g():
    return 1, 2


# x, y = g()
#print(x)
#print(y)


# m = 55
# n = 38
#
# print(m, n)
# m, n = n, m
# print(m, n)

# yield

def h(x):
    for i in range(x):
        print("生成", i)
        yield i


#t = h(9)
#print(type(t))


def run_func(f, *p, **q):
    import time
    bt = time.time()
    f(*p,**q)
    et = time.time()
    print("消耗时间:",et-bt)


# run_func(h,9)


#函数装饰器


def cost_time(a_func):
    from time import time

    def inner(*a, **b):
        bt = time()
        k = a_func(*a, **b)
        et = time()
        print("耗时:", et-bt)
        return k
    return inner


@cost_time
def rnd_cost(m):
    print("rnd_cost开始 with",m)
    from random import random
    x = random()
    from time import sleep
    sleep(x*5)
    print("rnd_cost结束")
    return x


t = rnd_cost("think")
print(t)
