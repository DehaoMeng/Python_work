#!/usr/bin/python3
# @File: 验证号码格式.py
# --coding: utf-8--
# @Author: 昊昊反思
# @Time: 2021年 11月 23日 22:41
'''
说明:
'''
import re

def china_mobile_phone(mobile_num):
    if(re.findall("^(\(\d{3}\)|\d{3}-)?\d{8}$",mobile_num,flags=0) != None):
        print("这是有效的电话号码格式")
    else:
        print("这不是有效的电话号码格式")

def china_post_num(post_num):
    if (re.findall("^\d{6}$", post_num, flags=0) != None):
        print("这是有效的邮政编码格式")
    else:
        print("这不是有效的邮政编码格式")

def web_num(url_num):
    if (re.findall("^https?://\w+(?:\.[^\.]+)+(?:/.+)*$", url_num, flags=0) != None):
        print("这是有效的网站网址格式")
    else:
        print("这不是有效的网站网址格式")

if __name__ == "__main__":
    print("请输入要验证的号码格式")
    print("1.中国电话号码格式")
    print("1.邮政编码")
    print("3.网站网址格式")
    pro = int(input())
    if(1 == pro):
        mobile_num = input("请输入中国电话号码：")
        china_mobile_phone(mobile_num)
    elif(2 == pro):
        post_num = input("请输入中国国内的邮政编码：")
        china_post_num(post_num)
    elif(3 == pro):
        url_num = input("请输入网址：")
        web_num(url_num)