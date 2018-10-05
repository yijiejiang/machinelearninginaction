from math import log
import operator

def createDataSet():
    dataSet = [[1, 1, 'yes'],
               [1, 1, 'yes'],
               [1, 0, 'no'],
               [0, 1, 'no'],
               [0, 1, 'no']]
    labels = ['no surfacing','flippers']
    #change to discrete values
    return dataSet, labels

def calcShannonEnt(dataSet):
    numEntries = len(dataSet)
    labelCounts = {}    # 声明一个变量保存实例总数，建立一个数据字典
    for featVec in dataSet: #the the number of unique elements and their occurance
        currentLabel = featVec[-1]      # 将最后一个数值作为键值保存
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
    shannonEnt = 0.0
    for key in labelCounts:
        prob = float(labelCounts[key])/numEntries       # prob只是过渡代数形式
        shannonEnt -= prob * log(prob,2) #log base 2
    return shannonEnt

myDat, labels = createDataSet()
print(myDat)
print(calcShannonEnt(myDat))