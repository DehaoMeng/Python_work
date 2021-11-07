#!/usr/bin/python3
# @File: Homework_Week6_3.py
# --coding: utf-8--
# @Author: 孟德昊
# @Time: 2021年 11月 07日 12:28
''' 说明:已知字典（自编3个键值对元素，包含姓名和电话号码等）。
   程序运行后，输入人名，

   若存在，则生成一个4位验证码，并输出相关信息。
   若不存在，则系统输出“该人不存在。'''
import random
if __name__ == "__main__":
    d = {"戴静彤" : "152-5297-9509",
         "Tony" : "177-8553-1795",
         "Mary" : "185-1759-1003"
         }
    name = input("请输入一个人名")
    if name in d.keys():
        print(random.randint(1000,10000))
        print(name,d[name])
    else:
        print("该人不存在")