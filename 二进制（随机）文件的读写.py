#!/usr/bin/python3
# @File: 二进制（随机）文件的读写.py
# --coding: utf-8--
# @Author: 昊昊反思
# @Time: 2021年 11月 23日 22:08
'''
说明:
'''
if __name__ == "__main__":
    with open('my.dat','wb') as fp:
        fp.write(b'Xiaoming\n')
        fp.write(b'student')
    with open('my.dat','rb') as fp:
        str = fp.read()
        print(str[-7:])