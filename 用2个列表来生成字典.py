#!/usr/bin/python3
# @File: 用2个列表来生成字典.py
# --coding: utf-8--
# @Author: 昊昊反思
# @Time: 2021年 11月 23日 23:10
'''
说明:
'''
if __name__ == "__main__":
    a = list(input().split(','))        #分别输入两个列表，列表中每个元素以逗号分隔
    b = list(input().split(','))
    c = {}                              #创建空字典
    if(len(a) >= len(b)):               #判断列表长度
        for i in range(len(b)):
            c[a[i]] = b[i]
    else:
        for i in range(len(a)):
            c[a[i]] = b[i]
    print(c)                            #打印字典