#!/usr/bin/python3
# @File: 折半查找法1.py
# --coding: utf-8--
# @Author: 孟德昊
# @Time: 2021年 11月 10日 15:40
'''说明:
用折半查找法查33和58在列表[1,13,26,33,45,55,68,72,83,99]中的位置，
非递归的方法来实现
列表[1,13,26,33,45,55,68,72,83,99]中各元素的数值从命令行参数中获取。
'''
import sys

def compare(a,c,max,min,mid):       #判断函数
    for i in range(len(a)):
        if ( c == a[min] ):
            print("关键词{}在列表中的索引是：{}".format(c,min))
            break
        elif ( c == a[max] ):
            print("关键词{}在列表中的索引是：{}".format(c,max))
            break
        elif ( c == a[mid] ):
            print("关键词{}在列表中的索引是：{}".format(c,mid))
            break
        elif ( c > a[mid]) :
            mid = int((mid + max + 1 ) / 2)
        elif ( c < a[mid] ):
            mid = int((mid + min ) / 2)
    if(i == 9):
        print("关键词{}不在该列表中".format(c))

if __name__ == "__main__":
    a = []  #创建空列表
    for i in range(1,11):   #输入列表
        b = int(sys.argv[i])
        a.append(b)
    min = 0         #初始最小值的索引
    max = 9         #初始最大值的索引
    mid = 4         #初始中值的索引
    compare(a, 33, max, min, mid)           #调用函数
    compare(a, 58, max, min,mid)
    #
    # min = 0
    # max = 9
    # mid = int (( max + min + 1 ) / 2 )
    # c = 58
    # for i in range(len(a)):
    #     if ( c == a[min] ):
    #         print("关键词{}在列表中的索引是：{}".format(c,min))
    #         break
    #     elif ( c == a[max] ):
    #         print("关键词{}在列表中的索引是：{}".format(c,max))
    #         break
    #     elif ( c == a[mid] ):
    #         print("关键词{}在列表中的索引是：{}".format(c,mid))
    #         break
    #     elif ( c > a[mid]) :
    #         min = mid
    #         mid = int((mid + max + 1 ) / 2)
    #     elif ( c < a[mid] ):
    #         max = mid
    #         mid = int((mid + min ) / 2)
    #
    # if(i == 9):
    #     print("关键词{}不在该列表中".format(c))
