#!/usr/bin/python3
# @File: 集合及其关系程序.py
# --coding: utf-8--
# @Author: 昊昊反思
# @Time: 2021年 11月 23日 20:26
'''说明:
随机生成10个从0~10区间内（包含0和10）的整数，分别组成集合A、集合B，输出A和B的内容、长度、最大值、最小值，以及A和B的并集、交集和差集
'''
import random
if __name__ == "__main__":
    A = set()
    B = set()
    for i in range(10):
        A.add(random.randint(0, 11))
    for i in range(10):
        B.add(random.randint(0, 11))
    print(A)
    print(len(A))
    print(max(A))
    print(min(A))
    print(B)
    print(len(B))
    print(max(B))
    print(min(B))
    print(A&B)
    print(A|B)
    print(A.difference(B))