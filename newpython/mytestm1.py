from random import random
v = [random() for i in range(1024)]
print(v)


def gt075(x):
    return x > 0.75


w = map(lambda x: x > 0.75, v)
print(w)
print(type(w))
print(all(w))

x = 55
y = 7
z = divmod(x, y)
print(z)


s = "x + y"
print(eval(s))


t= "k = x + y"
exec(t)
print(t)


w = filter(lambda x: x > 0.75, v)
print(w)
print(w.__sizeof__())

