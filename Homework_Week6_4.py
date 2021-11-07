#!/usr/bin/python3
# @File: Homework_Week6_4.py
# --coding: utf-8--
# @Author: 孟德昊
# @Time: 2021年 11月 07日 12:43
'''说明:输入并存储全班学生的成绩，输出平均成绩，最高成绩和最低成绩。
'''
if __name__ == "__main__":
    i = 0
    count = 0.0
    sys = {}
    while(1):
        name = input("请输入同学名称:(输入q以结束输入)")
        if name == "q":
            break
        grade = input("请输入同学成绩：")
        count += float(grade)
        i += 1
        sys[name] = float(grade)
    print(sys)
    new_sys1 = sorted(sys.values(),reverse=True)

    print("平均成绩为:{}".format(count/i))
    print("最高成绩为:{}".format(new_sys1[0]))
    print("最低成绩为:{}".format(new_sys1[i-1]))
