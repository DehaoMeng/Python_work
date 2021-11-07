#!/usr/bin/python3
# @File: Homework_Week7.py
# --coding: utf-8--
# @Author: 孟德昊
# @Time: 2021年 11月 07日 11:09
'''说明:
将下面一段文字分词后，统计词频。
要求：
1、输出频率最高的前2个词。
2、过滤掉长度小于2的词
3、以下2种均要输出：
  （1）是：极致,喜欢
  （2）是：极致    2
           喜欢    2'''


import jieba
jieba.setLogLevel(jieba.logging.INFO)

if __name__ == "__main__":
    txt ='''极致的喜欢，更像是一个自己与另一个自己在光阴里的隔世重逢。
    愿为对方毫无道理地盛开，会为对方无可救要地投入。
    这些都是极致的喜欢。——莫言'''
    txt = txt.replace(",", " ")
    txt = txt.replace(",", " ")
    txt = jieba.lcut(txt)

    d = {}
    for i in txt:
        if len(i) == 1:
            continue
        else:
            d[i] = d.get(i, 0) + 1
    ls1 = list(d.items())
    ls1.sort(key = lambda x : x[1], reverse=True)
    print("是:{},{}".format(ls1[0][0],ls1[1][0]))
    for i in range(2):
        x,y = ls1[i]
        if(i==0):
            print("是:{:<5}{:>2}".format(x,y))
        else:
            print("{:<5}{:>2}".format(x,y))