#!/usr/bin/python3
# @File: 斐波那契数列_递归.py
# --coding: utf-8--
# @Author: 昊昊反思
# @Time: 2021年 11月 23日 21:21
'''
说明:
'''

def fib(f,l):
    li = [1,1]
    for i in range(2,l+1):
        a = li[i - 1] + li[i - 2]
        li.append(a)
    for i in range(f-1,l):
        print(li[i])
if __name__ == "__main__":
    fib(10,20)