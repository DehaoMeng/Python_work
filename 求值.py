#!/usr/bin/python3
# @File: 求值.py
# --coding: utf-8--
# @Author: 昊昊反思
# @Time: 2021年 11月 30日 19:46
"""
说明:求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
"""

from math import pow


if __name__ == "__main__":
    """
    输入a值和n值
    """
    a = int(input())
    n = int(input())
    ls = []     # 创建空列表
    sum = 0     # 和为0
    for i in range(0,n):
        math = 0    # 每个值初值为0
        for j in range(0,i+1):      # 循环是math = a,aa,aaa,aaaa,……
            math = math + pow(10,j) * a
            # print(math)
        ls.append(math)     # 将值加入列表
    for i in ls:
        sum += i        # 求和
    print(sum)