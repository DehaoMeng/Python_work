#!/usr/bin/python3
# @File: 编写运算符重载.py
# --coding: utf-8--
# @Author: 孟德昊
# @Time: 2021年 11月 10日 17:31
'''说明:参照例9.23，编写运算符重载的程序
'''
class Mylist:
    def __init__(self,*args):
        self.__mylist = []
        for arg in args:
            self.__mylist.append(arg)

    def __add__(self, n):
        for i in range(0,len(self.__mylist)):
            self.__mylist[i] += n

    def __sub__(self, n):
        for i in range(0,len(self.__mylist)):
            self.__mylist[i] -= n

    def __mul__(self, n):
        for i in range(0, len(self.__mylist)):
            self.__mylist[i] *= n

    def __truediv__(self, n):
        for i in range(0, len(self.__mylist)):
            self.__mylist[i] /= n

    def __len__(self):
        return (len(self.__mylist))

    def __repr__(self):
        str1 = ''
        for i in range(0,len(self.__mylist)):
            str1 += str(self.__mylist) + ' '
        return str1


if __name__ == "__main__":
    m = Mylist(1,2,3,4,5)
    m + 2;print(repr(m))
    m - 2;print(repr(m))
    m * 2;print(repr(m))
    m / 2;print(repr(m))
    print(len(m))