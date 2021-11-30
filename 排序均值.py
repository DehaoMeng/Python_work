#!/usr/bin/python3
# @File: 排序均值.py
# --coding: utf-8--
# @Author: 昊昊反思
# @Time: 2021年 11月 30日 19:02
'''
说明: 随机产生10个两位的正整数，存入列表ls中，然后列表中的数进行排序（由小到大），最后分别输出：排序后的列表，这10个数的平均数，以及高于平均值的数的个数。
'''
# 导入随机包
from random import randint

ls = []  # 创建全局变量


def makerandommath():
    """
    随机生成十个二位正整数放入列表中
    """
    global ls
    for i in range(10):
        a = randint(10, 99)
        ls.append(a)


def sortedlist():
    """
    排序列表内的数值
    """
    global ls
    ls.sort(reverse=False)
    # print(ls)


def makeaverage():
    """
    求列表内数的平均数
    """
    sum = 0
    for i in range(len(ls)):
        sum += ls[i]
    average = sum / (i + 1)
    print(average)
    return average


def countbigger(average):
    """
    求列表中大于平均数的数的个数
    """
    count = 0
    for i in range(len(ls)):
        if average < ls[i]:
            count += 1
    print(count)


if __name__ == "__main__":
    makerandommath()
    sortedlist()
    average = makeaverage()
    countbigger(average)
