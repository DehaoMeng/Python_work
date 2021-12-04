"""
说明:编写程序实现功能：输出四位整数中所有的回文数。
"""
from math import pow
if __name__ == "__main__":
    for i in range(1000,10000):
        s = []
        for j in range(0,4):
            if j == 0:
                s.append(i%10)
            else:
                s.append(int(i // (pow(10, j)) % 10))
        for k in range(int(len(s) / 2)):
            if s[k] == s[len(s) - k - 1]:
                flag = 1
            else:
                flag = 0
                break
        if flag == 1:
            print(i,end=" ")