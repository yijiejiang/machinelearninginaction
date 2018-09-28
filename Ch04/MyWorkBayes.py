from numpy import *

def loadDataSet():      # 创建实验样本
    postingList=[['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
                 ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                 ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                 ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                 ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                 ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    classVec = [0, 1, 0, 1, 0, 1]    #1 is abusive, 0 not
    return postingList, classVec

def createVocabList(dataSet):       # 创建包含在所有文档中出现的不重复出现的词语的列表
    vocabSet = set([])  #create empty set
    for document in dataSet:
        vocabSet = vocabSet | set(document) #union of the two sets
    return list(vocabSet)   # 返回词汇表

def setOfWords2Vec(vocabList, inputSet):
    returnVec = [0]*len(vocabList)      # 创建一个其中所含元素都为零的向量
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] = 1
        else:
            print("the word: %s is not in my Vocabulary!" % word)
    return returnVec

list0posts, listClasses = loadDataSet()
myVocabList = createVocabList(list0posts)
# print(myVocabList)
print(setOfWords2Vec(myVocabList, list0posts[3]))