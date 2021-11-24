#!/usr/bin/python3
# @File: 斐波那契数列_迭代法.py
# --coding: utf-8--
# @Author: 昊昊反思
# @Time: 2021年 11月 23日 21:06
'''
说明:输出斐波那契数列的第10-20项——迭代法
'''
if __name__ == "__main__":
    li = [1,1]                      #将斐波那契数列的前两项放入到一个列表中
    for i in range(2,30):           #将斐波那契数列放入存入到列表中
        a = li[i-1] + li[i-2]
        li.append(a)
    for j in range(9,20):           #打印第10-20项斐波那契数列
        print(li[j])
