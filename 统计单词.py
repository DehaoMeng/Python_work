"""
说明:编写程序统计该字符串中每个单词出现的次数，对次数进行降序排列，并输出结果。
"""
import jieba
jieba.setLogLevel(jieba.logging.INFO)
if __name__ == "__main__":
    txt = 'Ladies and gentlemen, may I have your attention please:\
     We regret to announce that flight to Shanghai can not leave on schedule. \
     Thank you. Ladies and Gentlemen, may I have your attention please: \
     light  from Shanghai will arrive here. Thank you.'
    d = {}
    txt = txt.lower()
    txt = txt.replace(",", " ")
    txt = txt.replace(",", " ")
    txt = jieba.lcut(txt)
    for i in txt:
        if len(i) == 1:
            continue
        else:
            d[i] = d.get(i, 0) + 1
    ls1 = list(d.items())
    ls1.sort(key=lambda x: x[1], reverse=True)
    for i in range(0,len(ls1)):
        x, y = ls1[i]
        print("{:<5}{:>2}".format(x, y))
