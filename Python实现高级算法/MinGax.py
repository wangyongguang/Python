# -*- coding:utf-8 -*-
def greedy():
    n = 100 #表示加满油可行驶n公里
    k = 5   #旅途中有k个加油站
    d = [50,80,39,60,40,32] #表示加油站之间的距离
    num = 0 #表示加油次数
    for i in range(k):
        if d[i] > n:
            print('no solution') #如果距离中任何一个数值大于n 则无法计算
            return
    i,s = 0,0 #利用s进行迭代
    while i<=k:
        s+=d[i]
        if s>=n:
            s = d[i] #当局部和大于n则局部和更新为当前距离
            num += 1
            print("在第%d个加油站加油"%(i))
        i +=1
    print(num)
if __name__=='__main__':
    greedy()
