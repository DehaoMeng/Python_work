#!/usr/bin/python3
# @File: 判断回文.py
# --coding: utf-8--
# @Author: 昊昊反思
# @Time: 2021年 11月 23日 19:58
'''
说明:编写程序，判断用户输入的一个字符串是否为回文。如果是则输出True，否则输出Flase
'''
if __name__ == "__main__":
    a = list(input())
    # if(int(a / 100) == a % 10):
    #     print("True")
    # else:
    #     print("False")
    for i in range(len(a)):
        if(a[i] == a[len(a) - i - 1]):
            flag = 1
        else :
            flag = 0
            break
    if(1 == flag) :
        print("True")
    else :
        print("False")