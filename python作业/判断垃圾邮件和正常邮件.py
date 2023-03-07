from re import sub
from os import listdir
from collections import Counter
from itertools import chain
from numpy import array
from jieba import cut
from sklearn.naive_bayes import MultinomialNB

#存放所有文件中的单词
#每个元素是一个子列表,其中存放一个文件中的所有单词
allWords=[]

def getWordsFromFile(txtFile):
#获取每一封邮件中的所有词语
    words=[]
    with open(txtFile,encoding='utf8') as fp:
        for line in fp:
            #遍历每一行,删除两端的空白字符
            line= line.strip()
            #过滤干扰字符或无效字符
            line=sub(r'[.【】0-9、一 。 ，！~ \*]','', line)
            #分词
            line=cut(line)
            #过滤长度为1的词
            line=filter(lambda word:len(word)>1, line)
            words.extend(line)
    return words


def getTopNWords(topN):
    #按文件编号顺序处理当前文件夹中所有记事本文件
    #训练集中共151封邮件内容,0.txt 到126.txt 是垃圾邮件内
    #127.txt到150.txt为正常邮件内容
    txtFiles=[str(i)+',txt' for i in range (151)]
    #获取训练集中所有邮件中的全部单词
    for txtFile in txtFiles:
        allWords.append(getWordsFromFile(txtFile))
    #获取并返回出现次数最多的前 topN 个单词
    freq=Counter(chain(*allWords))
    return[w[0] for w in freq.most_common(topN)]

topWords=getTopNWords(600)

vector=[]
for words in allWords:
    temp=list(map(lambda x:words.count(x),topWords ))
    vector.append(temp)
vector=array(vector)
labels=array([1]*127+[0]*24)

model=MultinomialNB()
model.fit(vector,labels)
print(dir(model))

def predict(txtFile):
    words=getWordsFromFile(txtFile)
    currentVector=array(tuple(map(lambda x: words.count(x),topWords )))
    result=model.predict(currentVector.reshape (1,-1))[0]
    print(result)
    return '垃圾邮件' if result == 1 else '正常邮件'

print(predict('151.txt'))
print(predict('152.txt'))
print(predict('153.txt'))
print(predict('154.txt'))
print(predict('155.txt'))