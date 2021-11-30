#!/usr/bin/python3
# @File: 计算和返回第n阶调和数.py
# --coding: utf-8--
# @Author: 昊昊反思
# @Time: 2021年 11月 30日 18:54
"""
说明:定义计算和返回第n阶调和数（1+1/2+1/3+…+1/n）的函数，输出前n个调和数，n由用户输入。结果保留3位小数
"""
sum = 0
def Harmonic_number(n):
    """
    求1/n的值后递归求1+……+1/n的和
    """
    global sum
    if n != 1 :
        sum += 1 / n
        Harmonic_number(n-1)
    elif n == 1:
        sum += 1
        print("{:.3f}".format(sum))


if __name__ == "__main__":
    n = int(input())
    Harmonic_number(n)