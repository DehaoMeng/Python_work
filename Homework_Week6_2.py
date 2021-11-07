#!/usr/bin/python3
# @File: Homework_Week6_2.py
# --coding: utf-8--
# @Author: 孟德昊
# @Time: 2021年 11月 07日 11:44
''' 说明:编程：已知  txt=”love loves to love love.”
统计并输出 txt 中每个字符的个数。
要求：
（1）输出结果，需按字符个数的降序排列
（2）输出格式，要求除了功能实现以外，需要美观。
'''

if __name__ == "__main__":
    txt = " love loves to love love."
    d = {}
    for i in txt:
        if i != " ":
            d[i] = txt.count(i)
    d= sorted(d.items(), key = lambda d: d[1], reverse=True)
    for  i in range(len(d)):
        x , y = d[i]
        print("{}:{}".format(x,y))