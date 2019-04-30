from numpy import *
import operator
import matplotlib
import matplotlib.pyplot as plt

def createDataSet():
    group =array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group,labels

group,labels = createDataSet()
print(group);
print("---------------------------------------------------")

def classify0(inX,dataSet,labels,k): #KNN分类，inX表示向量，dataSet表示输入的样本集合，labels表示标签，k表示用于选择最近邻居的数
    dataSetSize = dataSet.shape[0]      #求维度
    diffMat = tile(inX,(dataSetSize,1)) - dataSet #将每个点的距离进行计算，tile函数另外做一个维度一样的初始数组
    sqDiffMat = diffMat**2  #求每个点与当前点的平方
    sqDistances = sqDiffMat.sum(axis=1)     #求距离的平方，axis=1表示横轴
    distances = sqDistances**0.5     #求距离
    print("各个距离为:",distances)
    sortedDistIndicies = distances.argsort()        #argsort函数返回的是数组值从小到大的索引值
    classCount = {}
    for i in range(k): #range(k) 表示从0到K-1
        voteIlabel = labels[sortedDistIndicies[i]]      #求出K个距离最近的标签
        classCount[voteIlabel] = classCount.get(voteIlabel,0)+1     #构造字典计算出现频率，get(A,B)函数获取字典，B表示如果没有就返回0
    sortedClassCount = sorted(classCount.items(),key=operator.itemgetter(1),reverse=True)       #iteritems()字典操作
    return sortedClassCount[0][0]   #返回频率最高的

tt = classify0([1.0,0.8],group,labels,3)
print(tt)
print("---------------------------------------------------")

x = arange(1,10) #实例2设置X轴
print(group[:,0])

fig = plt.figure()
ax1 = fig.add_subplot(111)
#设置标题
ax1.set_title('Scatter Plot')
#设置X轴标签
plt.xlabel('X')
#设置Y轴标签
plt.ylabel('Y')
#画散点图
ax1.scatter(group[:,0],group[:,1],c = 'r',marker = 'o')
#设置图标
plt.legend('x1')
#显示所画的图
plt.show()