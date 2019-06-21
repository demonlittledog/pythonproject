s = input("请输入数量")
try:
    n = int(s)
except ValueError as ve:
    print("输入错误，按0处理")
    n = 0
if n < 0:
    print("数量有误")
else:
    print("总价格%d"%(n*12))