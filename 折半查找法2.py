#!/usr/bin/python3
# @File: 折半查找法2.py
# --coding: utf-8--
# @Author: 孟德昊
# @Time: 2021年 11月 10日 15:50
'''说明:
用折半查找法查33和58在列表[1,13,26,33,45,55,68,72,83,99]中的位置，
用递归的方法来实现。
'''
import sys
def find_num(a,c,min,max,mid):
    if(max - mid >= 1):
        if ( c == a[min] ):
            print("关键词{}在列表中的索引是：{}".format(c,min))
        elif ( c == a[max] ):
            print("关键词{}在列表中的索引是：{}".format(c,max))
        elif ( c == a[mid] ):
            print("关键词{}在列表中的索引是：{}".format(c,mid))
        elif ( c > a[mid]) :
            min = mid
            mid = int((mid + max + 1 ) / 2)
            find_num(a, c, min, max, mid)
        elif ( c < a[mid] ):
            max = mid
            mid = int((mid + min ) / 2)
            find_num(a, c, min, max,mid)
    else:
        print("关键词{}不在该列表中".format(c))

if __name__ == "__main__":
    a = []
    for i in range(1, 11):
        b = int(sys.argv[i])
        a.append(b)
    # print(a)
    find_num( a, 33, 0, 9, 4 )
    find_num( a, 58, 0, 9, 4 )