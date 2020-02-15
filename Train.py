# python3.5
# -*- coding: utf-8 -*-

import jieba
import sys
import pandas as pd
import jieba.analyse
import math
import numpy as np
# 添加自定义词典
jieba.load_userdict("/Users/Viola/Desktop/WBFL/yinshang_dict_utf.txt")
from sklearn.cluster import KMeans
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
import re


# 导入数据
def get_data():
    data = pd.read_excel("/Users/Viola/Desktop/问题19/银行问题.xlsx")
    return data['信件内容']


# 分词
def cutwords(word):
    cutlist = []
    for num in range(len(word)):
        seg_list = jieba.cut(word[num],cut_all=False)
        cutlist.append(" ".join(seg_list))
    return cutlist


# 去除停用词
def delstopwords(data):
    file = open("/Users/Viola/Desktop/WBFL/Stopwords_utf.txt")
    stopword =file.read().replace("\n","")
    lists = []
    for worda in cutwords(data):
        for wordb in worda.split(" "):
            if wordb not in stopword:
              listes = re.sub("[A-Za-z0-9]","",wordb)
              lists.append(listes)
    return ' '.join(lists)

def get_dict():
    test_list = delstopwords(get_data())
    # 将文本中的词语转换为词频矩阵,矩阵元素a[i][j]表示j词在i类文本下的词频
    vectorizer = CountVectorizer()
    # 该类会统计每个词语的tf-idf权值
    transformer = TfidfTransformer()
    # 第一个fit_transform是计算tf-idf,第二个fit_transform是将文本转为词频矩阵
    ll = vectorizer.fit_transform([test_list])
    tfidf = transformer.fit_transform(vectorizer.fit_transform([test_list]))
    # 获取词袋模型中的所有词语
    word = vectorizer.get_feature_names()
    # 将tf-idf矩阵抽取出来,元素w[i][j]表示j词在i类文本中的tf-idf权重
    weight = tfidf.toarray()
    key_word = pd.DataFrame(word)
    key_weight = pd.DataFrame(weight)
    with open("/Users/Viola/Desktop/1016/银行问题.csv",'a') as tmp:
        key_word.to_csv(tmp,header=True,encoding="gb18030",index=False)
    with open("/Users/Viola/Desktop/1016/银行问题权重.csv",'a') as tmp:
        key_weight.to_csv(tmp,header=True,encoding="gb18030",index=False)


data = get_dict()