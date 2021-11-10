#!/usr/bin/python3
# @File: 输出面积.py
# --coding: utf-8--
# @Author: 孟德昊
# @Time: 2021年 11月 10日 17:15
'''说明:
在例9.21的基础上，修改父类Dimension中的area函数，该函数就输出一行话“形状没定，无法计算面积！”。
然后再增加一个三角形的类Triangle，在其中定义构造函数、计算面积的函数area。最后分别创建圆形、矩形、三角形的对象，然后输出它们的面积。
'''
from math import sqrt
class Dimension:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def area(self):
        print("形状没定，无法计算面积！")

class Circle(Dimension):
    def __init__(self,r):
        Dimension.__init__(self,r,0,0)

    def area(self):
        return 3.14 * self.x * self.x

class Rectangle(Dimension):
    def __init__(self,w,h):
        Dimension.__init__(self,w,h,0)
    def area(self):
        return self.x * self.y

class Triangle(Dimension):
    def __init__(self,a,b,c):
        Dimension.__init__(self,a,b,c)
    def area(self):
        p = (self.x + self.y + self.z)/2
        return sqrt( p * ( p - self.x ) * ( p - self.y ) * ( p - self.z ))
if __name__ == "__main__":
    circle = Circle(1)
    rectangle = Rectangle(1,2)
    triangle = Triangle(2,2,2)
    print(circle.area())
    print(rectangle.area())
    print(triangle.area())
