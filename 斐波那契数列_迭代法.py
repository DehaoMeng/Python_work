#!/usr/bin/python3
# @File: 斐波那契数列_迭代法.py
# --coding: utf-8--
# @Author: 昊昊反思
# @Time: 2021年 11月 23日 21:06
'''
说明:
'''
if __name__ == "__main__":
    li = [1,1]
    for i in range(2,100):
        a = li[i-1] + li[i-2]
        li.append(a)
    for j in range(9,20):
        print(li[j])
