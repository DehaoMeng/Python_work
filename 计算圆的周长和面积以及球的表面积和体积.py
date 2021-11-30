#!/usr/bin/python3
# @File: 计算圆的周长和面积以及球的表面积和体积.py
# --coding: utf-8--
# @Author: 昊昊反思
# @Time: 2021年 11月 30日 18:32
"""
说明:编写程序，创建类MyMath，计算圆的周长和面积以及球的表面积和体积，半径等参数由用户输入，编写测试代码，结果均保留两位小数
"""


class MyMath(object):
    def __init__(self, r):
        """
        初始化类
        """
        self.r = r
        self.PI = 3.14

    def printcircularperimeter(self):
        """
        圆的周长
        """
        print("{:.2f}".format(2 * self.PI * self.r))

    def printcirculararea(self):
        """
        圆的面积
        """
        print("{:.2f}".format(self.r * self.r * self.PI))

    def printballSurface_area(self):
        """
        球的表面积
        """
        print("{:.2f}".format(4 * self.PI * self.r * self.r))

    def printballvolume(self):
        """
        球的体积
        """
        print("{:.2f}".format(4 * self.PI * self.r * self.r * self.r / 3))


if __name__ == "__main__":
    r = int(input())  # 用户输入半径
    mymath = MyMath(r)  # 创建实例化对象
    """
    调用类中的函数
    """
    mymath.printcircularperimeter()
    mymath.printcirculararea()
    mymath.printballSurface_area()
    mymath.printballvolume()
