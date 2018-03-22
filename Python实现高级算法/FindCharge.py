# -*- coding:utf-8 -*-
def main():
    d = [0.01,0.02,0.05,0.1,0.2,0.5,1.0]#存储每种硬币面值
    d_num = [] #存储每种硬币的数量
    s = 0 #拥有零钱的总和
    temp = input('请输入每种零钱的数量：')
    d_num0 = temp.split(" ")

    for i in range(0,len(d_num0)):
        d_num.append(int(d_num0[i]))
        s +=d[i] * d_num[i] #计算出收银员拥有多少钱

    sum = float(input(""))
    if sum > s: #当输入金额比收银员的总额多时，无法找零
        print("数据有错")
        return 0

    s = s - sum #要想用的钱币数量最少，需要用大面值的钱币，因此从大元素开始遍历
    i = 6
    while i>=0:
        if sum >= d[i]:
            n = int(sum/d[i])
            if n >= d_num[i]:
                n = d_num[i] #更新n
            sum -= n* d[i] #贪心的关键步骤，令sum动态变化
            print("用了%d个%f元硬币"%(n,d[i]))
        i -= 1

if __name__=="__main__":
    main()


