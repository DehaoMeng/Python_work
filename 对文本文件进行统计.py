#!/usr/bin/python3
# @File: 对文本文件进行统计.py
# --coding: utf-8--
# @Author: 昊昊反思
# @Time: 2021年 11月 23日 22:20
'''
说明:
'''
import re
import collections
def analyze_text(text):
    paragh = re.split("\n\n", text)
    paragh_count = len(paragh)
    print("段落数：{}".format(paragh_count))
    lines = re.split("\n", text)
    lines_count = len(lines)
    print("行数：{}".format(lines_count))
    sentences = re.split("[.?!]", text)
    sentences_count = len(sentences)
    print("行数：{}".format(sentences_count))
    words = re.split(r"\W+", text)
    words_count = len(words)
    print("单词数：{}".format(words_count))
    freqs = collections.Counter(words)
    for w,m in freqs.items():
        if(w != ''):
            print(w,m)

if __name__ == "__main__":
    filename = "abstract.txt"
    with open(filename, 'r') as fp:
        test = fp.read()
    analyze_text(test.strip())