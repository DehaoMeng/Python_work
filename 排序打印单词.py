#!/usr/bin/python3
# @File: 排序打印单词.py
# --coding: utf-8--
# @Author: 昊昊反思
# @Time: 2021年 11月 30日 19:22
"""
说明:编写一个程序，接收一系列单个空格分隔的单词作为输入，在删除所有重复的单词并按字母升序排序后打印这些单词。
假设向程序提供以下输入:
hello world and practice makes perfect and hello world again
则输出为:
again and hello makes perfect practice world

"""


def setup_letter_list(ls1):
    """
    设置列表内不重复且不包含空格的字母
    """
    ls2 = []
    for i in ls1:
        if i not in ls2 and i != ' ':
            ls2.append(i)
    return ls2


def sort_list(ls4):
    """
    排序并输出
    """
    ls4.sort()
    for i in ls4 :
        print("{}".format(i),end=" ")


if __name__ == "__main__":
    # 输入列表以空格分开每个单词
    ls = list(input().split(" "))
    ls3 = setup_letter_list(ls)
    sort_list(ls3)

