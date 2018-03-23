# -*- encoding:utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
def greedy():
    #Packet = [100,150,200,400,600,800,1200,1400,1600,1800,2000,2200] #待传输的数据包大小
    np.random.seed(0) #确定种子使以后每次生成的随机数相同
    Packet = np.random.randint(1,8193,5) #这里要注意：随机分布是每个数据包1-1471，或1-8192或这5个总和是8192
    print ( "原始数据包列表为：" , Packet )
    Frag_Packet =[] #分片后的数据包数组
    i,j = 0,0
    for i in range(len(Packet)):
        n = int(Packet[i]/1471) #最大有效载荷1471byte的数据包个数
        re = Packet[i] % 1471 #大包取余后的小数据包
        while n > 0:
            n = n - 1 #这个j自动减1的目的是减去取余后的那个数据包
            Frag_Packet.append(1471)
        Frag_Packet.append(re) #
    sorted_Frag_packet=sorted(Frag_Packet,reverse=True)#对分片的数据包进行从大到小排序
    print ( "分片后的原始数据包列表：" , Frag_Packet )
    print ( "分片后经过排序的原始数据包列表：" , sorted_Frag_packet ) #以上是数据包分片及排序算法，下面是数据包融合算法

    sfp=[[0]*2 for i in range(len(sorted_Frag_packet))] #重新定义排序分片数据包sorted_Frag_packet为二维数组，第二列0和1表示该数据包是否聚合过
    for i in range(0,len(sorted_Frag_packet)): #对这些排序的packet进行标记，刚开始都没有进行融合的，都赋值为0
        sfp[i][0]=sorted_Frag_packet[i]
        sfp[i][1]=0
    print("重新定义排序的分片数据包",sfp)

    sfp_sum = 0.0 #从排序的数据包softed_Frag_packet中选择一部分数据包进行融合求和


    sub_sfp_sum = [[0 for i in range(len(sorted_Frag_packet))] for i in range(len(sorted_Frag_packet))]
    #定义使sfp_sum接近且小于1471的子集合


    aggr_Packet = [] #将融合后满足条件(sfp_sum<=1471)的数据包放入新的列表数组中
    for i in range(len(sorted_Frag_packet)): #外层循环，依次选定某个packet作为桩并跟后面的packet进行求和
        j=i      #内层循环，从这个第i个packet开始与sum累加，找到能够融合的packet
        #sub = []  # 用于存储子集合变量
        while j<len(sorted_Frag_packet): #判断内层循环是否超过数据包个数
            if sfp[j][1]==1: #先判断第j个packet是否被融合过
                j=j+1 #被融合过
                continue #跳过本次循环的剩余语句（下面的就不要运行了），j+1后继续下一个packet的while循环
            else:
                sfp_sum = sfp_sum + sfp[j][0] #从当前第i=j数据包开始计算并寻找最大的几个packet融合-贪心算法-次优解
            if sfp_sum==1471: #当一部分数据包融合正好等于1471，将sfp_sum附加到aggr_packet的末尾
                #aggr_Packet[i]=aggr_Packet.append(sfp[j][0])
                sub_sfp_sum[i] = sub_sfp_sum.append(sfp[j][0])
               # sub_sfp_sum[i]=sub_sfp_sum[i].append(sub)
                sfp[j][1]=1
                #sfp_sum = 0 #并将sfp_sum赋值为0
                break #停止执行最深层次的while循环，到外层的for循环继续
            elif sfp_sum<1471:
                #sub = sub.append ( sfp[j][0] )
                sub_sfp_sum[i].append ( sfp[j][0])
                #aggr_Packet[i] = aggr_Packet.append ( sfp[j][0] )
                sfp[j][1]=1
                j=j+1
                continue
            else:
                sfp_sum = sfp_sum - sfp[j][0]
                #print ( "组成贪心算法的子数据包集合：" , sub_sfp_sum[i].append ( sfp[j][0] ) )
                #如果加上当前数据包总和大于1471，则sum回退到上一个packet，并接着从更小的packet寻找即j=j+1
                #aggr_Packet.append(sfp_sum)
                j = j+1
        aggr_Packet.append ( sfp_sum )
        sfp_sum = 0

    print ( "组成贪心算法的子数据包集合：" , sub_sfp_sum)
    print("分片后经过排序并融合后的原始数据包列表：",aggr_Packet)


if __name__ =="__main__":
    greedy()
