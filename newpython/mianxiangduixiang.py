#python面向对象
#一切都是对象object
#定义类用class
#只要赋新的值就相当于new了一个新的对象，如果这样的话可以在前面不赋值
class People:
    age = 5
    pass
x = People()
y = People()
print(x.age)
x.age = 6
y.age = 5
print(x.age)
print(y.age)
#只要赋新的值就相当于new了一个新的对象，如果这样的话可以在前面不赋值
print(id(x.age))
print(id(People.age))
print(id(y.age))


class People:
    """类文档"""
    def __init__(self, a, n):
        self.age = a
        self.name = n
    def age(self,a):
        self.age = a
    def eat(self):
        print("吃饭")
        print(id(self))
    def __repr__(self):
        return "{%s:%d}"%(self.name, self.age)
    def __str__(self):
        return "年龄%d岁的%s"%(self.age, self.name)
    def __gt__(self, other):
        return self.age > other.age
x = People(5, 'Tom')
print(x)
y = People(3, 'jerry')
print(y)
a=(x,y)
print(a)
if x>y:
    print(x,"比",y,"大")

print(People.__doc__)


class People:
    count = 0

x = People()
x.count = 5
print(x.count)
print(People.count)