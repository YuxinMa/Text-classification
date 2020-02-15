#/usr/bin/env python3.5
# -*- coding: UTF-8 -*-

import pandas as pd


def fee_get_dict():
    fls = open('/Users/Viola/Desktop/问题19/utf/乱收费乱罚款乱检查.txt', 'r', errors="ignore")
    dictdata = fls.read().replace("\n"," ")
    return dictdata

def fee_get_dict_weight():
    dictweight = pd.read_csv(open('/Users/Viola/Desktop/问题19/utf/乱收费乱罚款乱检查权重.csv', errors="ignore", encoding="gb18030"))
    return dictweight['权重']

def traffic_get_dict():
    fls = open('/Users/Viola/Desktop/问题19/utf/交通驾管.txt', 'r', errors="ignore")
    dictdata = fls.read().replace("\n"," ")
    return dictdata

def traffic_get_dict_weight():
    dictweight = pd.read_csv(open('/Users/Viola/Desktop/问题19/utf/交通驾管权重.csv', errors="ignore", encoding="gb18030"))
    return dictweight['权重']

def stop_get_dict():
    fls = open('/Users/Viola/Desktop/问题19/utf/停车问题.txt', 'r', errors="ignore")
    dictdata = fls.read().replace("\n"," ")
    return dictdata

def stop_get_dict_weight():
    dictweight = pd.read_csv(open('/Users/Viola/Desktop/问题19/utf/停车问题权重.csv', errors="ignore", encoding="gb18030"))
    return dictweight['权重']

def bus_get_dict():
    fls = open('/Users/Viola/Desktop/问题19/utf/公交问题.txt', 'r', errors="ignore")
    dictdata = fls.read().replace("\n"," ")
    return dictdata

def bus_get_dict_weight():
    dictweight = pd.read_csv(open('/Users/Viola/Desktop/问题19/utf/公交问题权重.csv', errors="ignore", encoding="gb18030"))
    return dictweight['权重']

def public_get_dict():
    fls = open('/Users/Viola/Desktop/问题19/utf/公共服务窗口质量.txt', 'r', errors="ignore")
    dictdata = fls.read().replace("\n"," ")
    return dictdata

def public_get_dict_weight():
    dictweight = pd.read_csv(open('/Users/Viola/Desktop/问题19/utf/公共服务窗口质量权重.csv', errors="ignore", encoding="gb18030"))
    return dictweight['权重']

def police_get_dict():
    fls = open('/Users/Viola/Desktop/问题19/utf/公安消防.txt', 'r', errors="ignore")
    dictdata = fls.read().replace("\n"," ")
    return dictdata

def police_get_dict_weight():
    dictweight = pd.read_csv(open('/Users/Viola/Desktop/问题19/utf/公安消防权重.csv', errors="ignore", encoding="gb18030"))
    return dictweight['权重']

def taxi_get_dict():
    fls = open('/Users/Viola/Desktop/问题19/utf/出租车问题.txt', 'r', errors="ignore")
    dictdata = fls.read().replace("\n"," ")
    return dictdata

def taxi_get_dict_weight():
    dictweight = pd.read_csv(open('/Users/Viola/Desktop/问题19/utf/出租车问题权重.csv', errors="ignore", encoding="gb18030"))
    return dictweight['权重']

def insur_get_dict():
    fls = open('/Users/Viola/Desktop/问题19/utf/劳保社保.txt', 'r', errors="ignore")
    dictdata = fls.read().replace("\n"," ")
    return dictdata

def insur_get_dict_weight():
    dictweight = pd.read_csv(open('/Users/Viola/Desktop/问题19/utf/劳保社保权重.csv', errors="ignore", encoding="gb18030"))
    return dictweight['权重']

def medical_get_dict():
    fls = open('/Users/Viola/Desktop/问题19/utf/医疗卫生.txt', 'r', errors="ignore")
    dictdata = fls.read().replace("\n"," ")
    return dictdata

def medical_get_dict_weight():
    dictweight = pd.read_csv(open('/Users/Viola/Desktop/问题19/utf/医疗卫生权重.csv', errors="ignore", encoding="gb18030"))
    return dictweight['权重']

def city_get_dict():
    fls = open('/Users/Viola/Desktop/问题19/utf/城市建设.txt', 'r', errors="ignore")
    dictdata = fls.read().replace("\n"," ")
    return dictdata

def city_get_dict_weight():
    dictweight = pd.read_csv(open('/Users/Viola/Desktop/问题19/utf/城市建设权重.csv', errors="ignore", encoding="gb18030"))
    return dictweight['权重']

def busi_get_dict():
    fls = open('/Users/Viola/Desktop/问题19/utf/工商税务.txt', 'r', errors="ignore")
    dictdata = fls.read().replace("\n"," ")
    return dictdata

def busi_get_dict_weight():
    dictweight = pd.read_csv(open('/Users/Viola/Desktop/问题19/utf/工商税务权重.csv', errors="ignore", encoding="gb18030"))
    return dictweight['权重']

def disturb_get_dict():
    fls = open('/Users/Viola/Desktop/问题19/utf/扰民问题.txt', 'r', errors="ignore")
    dictdata = fls.read().replace("\n"," ")
    return dictdata

def disturb_get_dict_weight():
    dictweight = pd.read_csv(open('/Users/Viola/Desktop/问题19/utf/扰民问题权重.csv', errors="ignore", encoding="gb18030"))
    return dictweight['权重']

def service_get_dict():
    fls = open('/Users/Viola/Desktop/问题19/utf/政务服务窗口质量.txt', 'r', errors="ignore")
    dictdata = fls.read().replace("\n"," ")
    return dictdata

def service_get_dict_weight():
    dictweight = pd.read_csv(open('/Users/Viola/Desktop/问题19/utf/政务服务窗口质量权重.csv', errors="ignore", encoding="gb18030"))
    return dictweight['权重']

def environ_get_dict():
    fls = open('/Users/Viola/Desktop/问题19/utf/政务环境.txt', 'r', errors="ignore")
    dictdata = fls.read().replace("\n"," ")
    return dictdata

def environ_get_dict_weight():
    dictweight = pd.read_csv(open('/Users/Viola/Desktop/问题19/utf/政务环境权重.csv', errors="ignore", encoding="gb18030"))
    return dictweight['权重']

def credit_get_dict():
    fls = open('/Users/Viola/Desktop/问题19/utf/政府和企业失信.txt', 'r', errors="ignore")
    dictdata = fls.read().replace("\n"," ")
    return dictdata

def credit_get_dict_weight():
    dictweight = pd.read_csv(open('/Users/Viola/Desktop/问题19/utf/政府和企业失信权重.csv', errors="ignore", encoding="gb18030"))
    return dictweight['权重']

def effic_get_dict():
    fls = open('/Users/Viola/Desktop/问题19/utf/效能建设.txt', 'r', errors="ignore")
    dictdata = fls.read().replace("\n"," ")
    return dictdata

def effic_get_dict_weight():
    dictweight = pd.read_csv(open('/Users/Viola/Desktop/问题19/utf/效能建设权重.csv', errors="ignore", encoding="gb18030"))
    return dictweight['权重']

def water_get_dict():
    fls = open('/Users/Viola/Desktop/问题19/utf/水电煤气.txt', 'r', errors="ignore")
    dictdata = fls.read().replace("\n"," ")
    return dictdata

def water_get_dict_weight():
    dictweight = pd.read_csv(open('/Users/Viola/Desktop/问题19/utf/水电煤气权重.csv', errors="ignore", encoding="gb18030"))
    return dictweight['权重']

def comm_get_dict():
    fls = open('/Users/Viola/Desktop/问题19/utf/通讯传媒.txt', 'r', errors="ignore")
    dictdata = fls.read().replace("\n"," ")
    return dictdata

def comm_get_dict_weight():
    dictweight = pd.read_csv(open('/Users/Viola/Desktop/问题19/utf/通讯传媒权重.csv', errors="ignore", encoding="gb18030"))
    return dictweight['权重']

def bank_get_dict():
    fls = open('/Users/Viola/Desktop/问题19/utf/银行问题.txt', 'r', errors="ignore")
    dictdata = fls.read().replace("\n"," ")
    return dictdata

def bank_get_dict_weight():
    dictweight = pd.read_csv(open('/Users/Viola/Desktop/问题19/utf/银行问题权重.csv', errors="ignore", encoding="gb18030"))
    return dictweight['权重']