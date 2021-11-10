#!/usr/bin/python3
# @File: 猜数.py
# --coding: utf-8--
# @Author: 孟德昊
# @Time: 2021年 11月 10日 19:14
'''说明:随机产生一个0到100之间（包括0和100）的偶数，请用户猜测具体是哪个数，即：不断从标准输入读取用户的猜测值（用户每次输入一个偶数），
并根据猜测值给出提示信息：“太大”、“太小”或“正确!”
'''
from random import randrange

def compare(a,s):
    if ( a > s ):
        too_small()
    elif( a < s ):
        too_big()
    elif( a == s ):
        right()

def right():
    print("正确")

def too_small():
    print("太小")

def too_big():
    print("太大")
if __name__ == "__main__":
    a = randrange(0,101,2)
    # print(a)
    while(1):
        s = int(input("请输入一个偶数:"))
        compare(a,s)
        if(a == s):     #当猜中时不在循环
            break
