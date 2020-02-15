#/usr/bin/env python 3.5
# -*- coding: UTF-8 -*-
import math
import numpy as np


# 余弦相似度
def count_cos_distance(train_weight,test_weight):

    dot_product = np.dot(test_weight,train_weight)
    P = np.dot(train_weight,train_weight)
    train_weight_sqrt =math.sqrt(P)
    L = np.dot(test_weight,test_weight.T)
    test_weight_sqrt = math.sqrt(L)
    Q = dot_product/(train_weight_sqrt*test_weight_sqrt)

    return Q