#!/usr/bin/python3
# @File: 输出当前时间.py
# --coding: utf-8--
# @Author: 孟德昊
# @Time: 2021年 11月 10日 20:27
'''说明:编写一个程序，获取系统当前的时间等信息，输出格式如下面方框里所示。然后将这些信息写入一个文本文件，最后将文件中的内容读出来后显示在屏幕上。
第一行是时间和日期，第二行是星期几，第三行是本月有几天。
'''
from datetime import datetime
def days(month):
    a = [1,3,5,7,8,10,12]
    if month in a:
        return 31
    else:
        return 30

if __name__ == "__main__":
    date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(date_time)

    day = datetime.now().strftime("%A")
    print(day)
    month = datetime.now().strftime("%d")
    x = days(month)
    print("There are {} days in this month.".format(x))

    with open("datetime.txt","w",encoding="utf-8") as dt :
        dt.write(date_time+'\n')
        dt.write(day+'\n')
        dt.write("There are {} days in this month.".format(x))