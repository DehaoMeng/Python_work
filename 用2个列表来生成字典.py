#!/usr/bin/python3
# @File: 用2个列表来生成字典.py
# --coding: utf-8--
# @Author: 昊昊反思
# @Time: 2021年 11月 23日 23:10
'''
说明:
'''
if __name__ == "__main__":
    a = list(input().split(','))
    b = list(input().split(','))
    c = {}
    if(len(a) >= len(b)):
        for i in range(len(b)):
            c[a[i]] = b[i]
    else:
        for i in range(len(a)):
            c[a[i]] = b[i]
    print(c)