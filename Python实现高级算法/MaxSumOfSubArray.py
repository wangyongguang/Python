# -*- coding:utf-8 -*-
def main():
    s = [12,-4,32,-36,12,6,-6]
    print("定义的数组：",s)
    s_max,s_sum=0,0
    for i in range(len(s)):
        s_sum+=s[i]
        if s_sum>=s_max:
            s_max = s_sum #不断更新迭代s_max的值，尽可能的令其最大
        elif s_sum < 0:
            s_sum = 0
    print("最大数组和为：",s_max)
if __name__=="__main__":
    main()