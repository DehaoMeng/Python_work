"""
说明:编写程序：生成20个0-20之间的随机整数，并统计每个元素的出现次数。
"""

from random import randint

if __name__ == "__main__":
    c = []
    s = {}
    for i in range(20):
        a = randint(0, 21)
        c.append(a)
    for i in range(len(c)):
        if c[i] not in s.keys():
            s[c[i]] = 1
        else:
            s[c[i]] = s[c[i]] + 1
    for m,i in s.items():
        print(m,":",i)