# 汉诺塔问题:
# 有若干个盘子,从大到小,自底向上排列
# 有3个位置,A,B,C
# 如果所有盘子处于A位置,需移动到C位置
# 可以借助B作为临时存放位置
# 1, 每次只能移动一个盘子
# 2, 小盘子只能放在大盘子上边

# 描述n个盘子从哪移动到哪
# move(n,beginPlace,endPlace,tempPlace)
# move(2,'A','C','B')

def move(n,bp,ep,tp):
    if n==1:
        print('从%s移动到%s'%(bp,ep))
    # elif n==2:
    #     print('从%s移动到%s'%(bp,tp))
    #     print('从%s移动到%s'%(bp,ep))
    #     print('从%s移动到%s'%(tp,ep))
    else:
        move(n-1,bp,tp,ep)
        print('从%s移动到%s'%(bp,ep))
        move(n-1,tp,ep,bp)


move(3,'A','C','B')



