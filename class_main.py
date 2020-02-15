#/usr/bin/env python3.5
# -*- coding: UTF-8 -*-

import class_dict as dicts
import class_function as class_fun
import jieba
import pandas as pd
import jieba.analyse
# 添加自定义词典
jieba.load_userdict("/Users/Viola/Desktop/WBFL/yinshang_dict_utf.txt")
from sklearn.feature_extraction.text import TfidfVectorizer
import re

pd.set_option('max_rows',200)

# 切分词
def cutonesentent(test_word):
    seg_list = jieba.cut(test_word,cut_all=False)
    return " ".join(seg_list)

# 去除停用词
def delstoptestwords(testdata):
    file = open("/Users/Viola/Desktop/WBFL/Stopwords_utf.txt")
    stopword =file.read().replace("\n","")
    lists = []
    for worda in cutonesentent(testdata).split(" "):
        if worda not in stopword:
            liste= re.sub("[A-Za-z0-9]","",worda)
            lists.append(liste)
    return ' '.join(lists)

def get_test_data(nums):
    test_data = pd.read_excel("/Users/Viola/Desktop/问题19/Test_data.xlsx")
    test = test_data['信件内容']
    return test[nums]


def fee_get_similarity(num):
    test_list = delstoptestwords(get_test_data(num))
    tfidf_vectorizer = TfidfVectorizer(min_df = 1)
    #tfidf_matrix = tfidf_vectorizer.fit_transform([dicts.fee_get_dict()])
    tfidf_vectorizer.fit_transform([dicts.fee_get_dict()])
    new_term_freq_matrix = tfidf_vectorizer.transform([test_list])
    train_weight = dicts.fee_get_dict_weight()
    test_weight = new_term_freq_matrix.toarray()
    dist = class_fun.count_cos_distance(train_weight,test_weight)
    return dist

def taxi_get_similarity(num):
    test_list = delstoptestwords(get_test_data(num))
    tfidf_vectorizer = TfidfVectorizer(min_df = 1)
    #tfidf_matrix = tfidf_vectorizer.fit_transform([dicts.taxi_get_dict()])
    tfidf_vectorizer.fit_transform([dicts.taxi_get_dict()])
    new_term_freq_matrix = tfidf_vectorizer.transform([test_list])
    train_weight = dicts.taxi_get_dict_weight()
    test_weight = new_term_freq_matrix.toarray()
    dist = class_fun.count_cos_distance(train_weight,test_weight)
    return dist

def comm_get_similarity(num):
    test_list = delstoptestwords(get_test_data(num))
    tfidf_vectorizer = TfidfVectorizer(min_df = 1)
    #tfidf_matrix = tfidf_vectorizer.fit_transform([dicts.comm_get_dict()])
    tfidf_vectorizer.fit_transform([dicts.comm_get_dict()])
    new_term_freq_matrix = tfidf_vectorizer.transform([test_list])
    train_weight = dicts.comm_get_dict_weight()
    test_weight = new_term_freq_matrix.toarray()
    #print(train_weight, test_weight)
    dist = class_fun.count_cos_distance(train_weight,test_weight)
    return dist

def bus_get_similarity(num):
    test_list = delstoptestwords(get_test_data(num))
    tfidf_vectorizer = TfidfVectorizer(min_df = 1)
    #tfidf_matrix = tfidf_vectorizer.fit_transform([dicts.bus_get_dict()])
    tfidf_vectorizer.fit_transform([dicts.bus_get_dict()])
    new_term_freq_matrix = tfidf_vectorizer.transform([test_list])
    train_weight = dicts.bus_get_dict_weight()
    test_weight = new_term_freq_matrix.toarray()
    dist = class_fun.count_cos_distance(train_weight,test_weight)
    return dist

def bank_get_similarity(num):
    test_list = delstoptestwords(get_test_data(num))
    tfidf_vectorizer = TfidfVectorizer(min_df = 1)
    #tfidf_matrix = tfidf_vectorizer.fit_transform([dicts.bank_get_dict()])
    tfidf_vectorizer.fit_transform([dicts.bank_get_dict()])
    new_term_freq_matrix = tfidf_vectorizer.transform([test_list])
    train_weight = dicts.bank_get_dict_weight()
    test_weight = new_term_freq_matrix.toarray()
    dist = class_fun.count_cos_distance(train_weight,test_weight)
    return dist

def traffic_get_similarity(num):
    test_list = delstoptestwords(get_test_data(num))
    tfidf_vectorizer = TfidfVectorizer(min_df = 1)
    #tfidf_matrix = tfidf_vectorizer.fit_transform([dicts.traffic_get_dict()])
    tfidf_vectorizer.fit_transform([dicts.traffic_get_dict()])
    new_term_freq_matrix = tfidf_vectorizer.transform([test_list])
    train_weight = dicts.traffic_get_dict_weight()
    test_weight = new_term_freq_matrix.toarray()
    dist = class_fun.count_cos_distance(train_weight,test_weight)
    return dist

def stop_get_similarity(num):
    test_list = delstoptestwords(get_test_data(num))
    tfidf_vectorizer = TfidfVectorizer(min_df = 1)
    #tfidf_matrix = tfidf_vectorizer.fit_transform([dicts.stop_get_dict()])
    tfidf_vectorizer.fit_transform([dicts.stop_get_dict()])
    new_term_freq_matrix = tfidf_vectorizer.transform([test_list])
    train_weight = dicts.stop_get_dict_weight()
    test_weight = new_term_freq_matrix.toarray()
    dist = class_fun.count_cos_distance(train_weight,test_weight)
    return dist

def public_get_similarity(num):
    test_list = delstoptestwords(get_test_data(num))
    tfidf_vectorizer = TfidfVectorizer(min_df = 1)
    #tfidf_matrix = tfidf_vectorizer.fit_transform([dicts.public_get_dict()])
    tfidf_vectorizer.fit_transform([dicts.public_get_dict()])
    new_term_freq_matrix = tfidf_vectorizer.transform([test_list])
    train_weight = dicts.public_get_dict_weight()
    test_weight = new_term_freq_matrix.toarray()
    dist = class_fun.count_cos_distance(train_weight,test_weight)
    return dist

def police_get_similarity(num):
    test_list = delstoptestwords(get_test_data(num))
    tfidf_vectorizer = TfidfVectorizer(min_df = 1)
    #tfidf_matrix = tfidf_vectorizer.fit_transform([dicts.police_get_dict()])
    tfidf_vectorizer.fit_transform([dicts.police_get_dict()])
    new_term_freq_matrix = tfidf_vectorizer.transform([test_list])
    train_weight = dicts.police_get_dict_weight()
    test_weight = new_term_freq_matrix.toarray()
    dist = class_fun.count_cos_distance(train_weight,test_weight)
    return dist

def insur_get_similarity(num):
    test_list = delstoptestwords(get_test_data(num))
    tfidf_vectorizer = TfidfVectorizer(min_df = 1)
    #tfidf_matrix = tfidf_vectorizer.fit_transform([dicts.insur_get_dict()])
    tfidf_vectorizer.fit_transform([dicts.insur_get_dict()])
    new_term_freq_matrix = tfidf_vectorizer.transform([test_list])
    train_weight = dicts.insur_get_dict_weight()
    test_weight = new_term_freq_matrix.toarray()
    dist = class_fun.count_cos_distance(train_weight,test_weight)
    return dist

def medical_get_similarity(num):
    test_list = delstoptestwords(get_test_data(num))
    tfidf_vectorizer = TfidfVectorizer(min_df = 1)
    #tfidf_matrix = tfidf_vectorizer.fit_transform([dicts.medical_get_dict()])
    tfidf_vectorizer.fit_transform([dicts.medical_get_dict()])
    new_term_freq_matrix = tfidf_vectorizer.transform([test_list])
    train_weight = dicts.medical_get_dict_weight()
    test_weight = new_term_freq_matrix.toarray()
    dist = class_fun.count_cos_distance(train_weight,test_weight)
    return dist

def city_get_similarity(num):
    test_list = delstoptestwords(get_test_data(num))
    tfidf_vectorizer = TfidfVectorizer(min_df = 1)
    #tfidf_matrix = tfidf_vectorizer.fit_transform([dicts.city_get_dict()])
    tfidf_vectorizer.fit_transform([dicts.city_get_dict()])
    new_term_freq_matrix = tfidf_vectorizer.transform([test_list])
    train_weight = dicts.city_get_dict_weight()
    test_weight = new_term_freq_matrix.toarray()
    dist = class_fun.count_cos_distance(train_weight,test_weight)
    return dist

def busi_get_similarity(num):
    test_list = delstoptestwords(get_test_data(num))
    tfidf_vectorizer = TfidfVectorizer(min_df = 1)
    #tfidf_matrix = tfidf_vectorizer.fit_transform([dicts.busi_get_dict()])
    tfidf_vectorizer.fit_transform([dicts.busi_get_dict()])
    new_term_freq_matrix = tfidf_vectorizer.transform([test_list])
    train_weight = dicts.busi_get_dict_weight()
    test_weight = new_term_freq_matrix.toarray()
    dist = class_fun.count_cos_distance(train_weight,test_weight)
    return dist

def disturb_get_similarity(num):
    test_list = delstoptestwords(get_test_data(num))
    tfidf_vectorizer = TfidfVectorizer(min_df = 1)
    #tfidf_matrix = tfidf_vectorizer.fit_transform([dicts.disturb_get_dict()])
    tfidf_vectorizer.fit_transform([dicts.disturb_get_dict()])
    new_term_freq_matrix = tfidf_vectorizer.transform([test_list])
    train_weight = dicts.disturb_get_dict_weight()
    test_weight = new_term_freq_matrix.toarray()
    dist = class_fun.count_cos_distance(train_weight,test_weight)
    return dist

def service_get_similarity(num):
    test_list = delstoptestwords(get_test_data(num))
    tfidf_vectorizer = TfidfVectorizer(min_df = 1)
    #tfidf_matrix = tfidf_vectorizer.fit_transform([dicts.service_get_dict()])
    tfidf_vectorizer.fit_transform([dicts.service_get_dict()])
    new_term_freq_matrix = tfidf_vectorizer.transform([test_list])
    train_weight = dicts.service_get_dict_weight()
    test_weight = new_term_freq_matrix.toarray()
    dist = class_fun.count_cos_distance(train_weight,test_weight)
    return dist

def environ_get_similarity(num):
    test_list = delstoptestwords(get_test_data(num))
    tfidf_vectorizer = TfidfVectorizer(min_df = 1)
    #tfidf_matrix = tfidf_vectorizer.fit_transform([dicts.environ_get_dict()])
    tfidf_vectorizer.fit_transform([dicts.environ_get_dict()])
    new_term_freq_matrix = tfidf_vectorizer.transform([test_list])
    train_weight = dicts.environ_get_dict_weight()
    test_weight = new_term_freq_matrix.toarray()
    dist = class_fun.count_cos_distance(train_weight,test_weight)
    return dist

def credit_get_similarity(num):
    test_list = delstoptestwords(get_test_data(num))
    tfidf_vectorizer = TfidfVectorizer(min_df = 1)
    #tfidf_matrix = tfidf_vectorizer.fit_transform([dicts.credit_get_dict()])
    tfidf_vectorizer.fit_transform([dicts.credit_get_dict()])
    new_term_freq_matrix = tfidf_vectorizer.transform([test_list])
    train_weight = dicts.credit_get_dict_weight()
    test_weight = new_term_freq_matrix.toarray()
    dist = class_fun.count_cos_distance(train_weight,test_weight)
    return dist

def effic_get_similarity(num):
    test_list = delstoptestwords(get_test_data(num))
    tfidf_vectorizer = TfidfVectorizer(min_df = 1)
    #tfidf_matrix = tfidf_vectorizer.fit_transform([dicts.effic_get_dict()])
    tfidf_vectorizer.fit_transform([dicts.effic_get_dict()])
    new_term_freq_matrix = tfidf_vectorizer.transform([test_list])
    train_weight = dicts.effic_get_dict_weight()
    test_weight = new_term_freq_matrix.toarray()
    dist = class_fun.count_cos_distance(train_weight,test_weight)
    return dist

def water_get_similarity(num):
    test_list = delstoptestwords(get_test_data(num))
    tfidf_vectorizer = TfidfVectorizer(min_df = 1)
    #tfidf_matrix = tfidf_vectorizer.fit_transform([dicts.water_get_dict()])
    tfidf_vectorizer.fit_transform([dicts.water_get_dict()])
    new_term_freq_matrix = tfidf_vectorizer.transform([test_list])
    train_weight = dicts.water_get_dict_weight()
    test_weight = new_term_freq_matrix.toarray()
    dist = class_fun.count_cos_distance(train_weight,test_weight)
    return dist


if __name__:

    test_result = []
    for i in range(142):
        print(i)
        if water_get_similarity(i)[0]>0.055:
            end = ({'index': i, 'counent': get_test_data(i), 'similarity': water_get_similarity(i)[0], 'quest': "水电煤气"})
        elif medical_get_similarity(i)[0]>0.03:
            end = ({'index': i, 'counent': get_test_data(i), 'similarity': medical_get_similarity(i)[0], 'quest': "医疗卫生"})
        elif insur_get_similarity(i)[0]>0.06:
            end = ({'index': i, 'counent': get_test_data(i), 'similarity': insur_get_similarity(i)[0], 'quest': "劳保社保"})
        elif bus_get_similarity(i)[0]>0.03:
            end = ({'index': i, 'counent': get_test_data(i), 'similarity': bus_get_similarity(i)[0], 'quest': "公交问题"})
        elif taxi_get_similarity(i)[0]>0.05:
            end = ({'index': i, 'counent': get_test_data(i), 'similarity': taxi_get_similarity(i)[0], 'quest': "出租车问题"})
        elif police_get_similarity(i)[0]>0.17:
            end = ({'index': i, 'counent': get_test_data(i), 'similarity': police_get_similarity(i)[0], 'quest': "公安消防"})
        elif traffic_get_similarity(i)[0]>0.087:
            end = ({'index': i, 'counent': get_test_data(i), 'similarity': traffic_get_similarity(i)[0], 'quest': "交通驾管"})
        elif stop_get_similarity(i)[0]>0.029:
            end = ({'index': i, 'counent': get_test_data(i), 'similarity': stop_get_similarity(i)[0], 'quest': "停车问题"})
        elif comm_get_similarity(i)[0]>0.068:
            end = ({'index': i, 'counent': get_test_data(i), 'similarity': comm_get_similarity(i)[0], 'quest': "通讯传媒"})
        elif city_get_similarity(i)[0]>0.16:
            end = ({'index': i, 'counent': get_test_data(i), 'similarity': city_get_similarity(i)[0], 'quest': "城市建设"})
        elif bank_get_similarity(i)[0]>0.04:
            end = ({'index': i, 'counent': get_test_data(i), 'similarity': bank_get_similarity(i)[0], 'quest': "银行问题"})
        elif busi_get_similarity(i)[0]>0.06:
            end = ({'index': i, 'counent': get_test_data(i), 'similarity': busi_get_similarity(i)[0], 'quest': "工商税务"})
        elif fee_get_similarity(i)[0]>0.036:
            end = ({'index': i, 'counent': get_test_data(i), 'similarity': fee_get_similarity(i)[0], 'quest': "乱收费乱罚款乱检查"})
        elif credit_get_similarity(i)[0]>0.11:
            end = ({'index': i, 'counent': get_test_data(i), 'similarity': credit_get_similarity(i)[0], 'quest': "政府和企业失信"})
        elif disturb_get_similarity(i)[0]>0.16:
            end = ({'index': i, 'counent': get_test_data(i), 'similarity': disturb_get_similarity(i)[0], 'quest': "扰民问题"})
        elif environ_get_similarity(i)[0]>0.11:
            end = ({'index': i, 'counent': get_test_data(i), 'similarity': environ_get_similarity(i)[0], 'quest': "政务环境"})
        elif effic_get_similarity(i)[0]>0.095:
            end = ({'index': i, 'counent': get_test_data(i), 'similarity': effic_get_similarity(i)[0], 'quest': "效能建设"})
        elif public_get_similarity(i)[0]>0.087:
            end = ({'index': i, 'counent': get_test_data(i), 'similarity': public_get_similarity(i)[0], 'quest': "公共服务窗口质量"})
        elif service_get_similarity(i)[0]>0.13:
            end = ({'index': i, 'counent': get_test_data(i), 'similarity': service_get_similarity(i)[0], 'quest': "政务服务窗口质量"})
        else:
            end = ({'index': i, 'counent': get_test_data(i), 'similarity': service_get_similarity(i)[0], 'quest': "其它问题"})
        test_result.append(end)

    df = pd.DataFrame(test_result)
    with open("/Users/Viola/Desktop/问题19/Result.csv",'a') as temp1:
     df.to_csv(temp1,index=False,header=True,encoding="gb18030")



