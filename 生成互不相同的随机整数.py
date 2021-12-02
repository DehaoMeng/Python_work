"""
说明:编写程序：生成20个0-20之间的随机整数并输出其中互不相同的数。
"""

from random import randint

if __name__ == "__main__":
    c = []
    s = set()
    for i in range(20):
        a = randint(0,21)
        c.append(a)
    for i in range(20):
        if c[i] not in s :
            s.add(c[i])
    print(s)