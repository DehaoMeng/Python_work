#!/usr/bin/python3
# @File: 判断回文.py
# --coding: utf-8--
# @Author: 昊昊反思
# @Time: 2021年 11月 23日 19:58
'''
说明:编写程序，判断用户输入的一个字符串是否为回文。如果是则输出True，否则输出Flase
'''
if __name__ == "__main__":
    while(True):
        print("输入#号表示结束")
        a = list(input())       #输入一个字符串并将其每个元素分别存入到一个列表中
        if (a[0] != '#'):
            # if(int(a / 100) == a % 10):
            #     print("True")
            # else:
            #     print("False")
            for i in range(int(len(a)/2)):            #按输入列表的长度的一半查询是否对称
                if(a[i] == a[len(a) - i - 1]): #相等即为回文，否则不为回文。
                    flag = 1
                else :
                    flag = 0
                    break
            if(1 == flag) :
                print("True")
            else :
                print("False")
        else:
            break