from math import log

#计算给定数据集的香农熵
def calcShannoEnt(dataSet):
    numEntries = len(dataSet)   #计算实例总数
    labelCounts = {}
    for featVec in dataSet:
        currentLabel = featVec[-1]      #[1]取倒数第一个数据

        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] +=1
    shannoEnt = 0.0
    for key in labelCounts:
        prob = float(labelCounts[key])/numEntries
        shannoEnt -= prob*log(prob,2)
    return shannoEnt

def createDataSet():        #构造实例函数
    dataSet = [[1,1,'yes'],[1,1,'yes'],[1,0,'no'],[0,1,'no'],[0,1,'no'],]   #一共5个，也可以增加一个maybe的分类
    labels = ['no surfacing','flippers']

    return  dataSet,labels      #两个变量

dataSet,labels = createDataSet()
print(dataSet)

shannoEnt = calcShannoEnt(dataSet)
print("香农熵：",shannoEnt)
print("-----------------------------------------------------------------------------------------------------------------------")

#按照给定特征划分数据集
def splitDataSet(dataSet,axis,value):       #数据集，划分数据集的特征，需要返回特征的值
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            reducedFeatVec = featVec[:axis]     #添加该值之前的所有特征
            reducedFeatVec.extend(featVec[axis+1:])        #添加该值之后的所有特征
            retDataSet.append(reducedFeatVec)
    return retDataSet
retDataSet = splitDataSet(dataSet,1,1)      #第二个，是否为1

print("划分数据集",retDataSet)
print("-----------------------------------------------------------------------------------------------------------------------")


#选取最好的数据划分方式
def chooseBestFeatureTpSplit(dataSet):

    numFeature = len(dataSet[0]) - 1    #数据集合中的一个计算长度-1确定划分方式个数
    baseEntropy = calcShannoEnt(dataSet)    #计算原始香农熵
    bestInfoGain = 0.0
    bestFeature = -1

    for i in range(numFeature):     #range函数从0开始一直数

        # 创建唯一分类标签列表
        featList = [example[i] for example in dataSet]     #先弄第一个条件，然后是第二个条件，以此类推

        uniqueVals = set(featList)      #消除重复的得容构建一个class特征集合
        print("划分特征值的个数",uniqueVals)

        newEntropy = 0.0

        # 计算每种划分方式的信息熵
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet,i,value)      #划分数据集得到划分之后的数据集合

            prob = len(subDataSet)/float(len(dataSet))      # 划分之后的数据集内容个数 与 原始数据集内容个数之比值

            newEntropy += prob*calcShannoEnt(subDataSet)
        infoGain = baseEntropy - newEntropy

        if(infoGain > bestInfoGain):        #计算最好的信息熵
            bestInfoGain = infoGain
            bestFeature = i
    return bestFeature      #第x个特征是我们最好用于划分数据集的特征

bestFeature = chooseBestFeatureTpSplit(dataSet)

print(bestFeature)