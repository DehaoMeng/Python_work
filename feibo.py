"""
说明:2.	编写函数，参数为一个整数n。利用递归获取斐波那契数列中的第n个数并返回结果。
"""


def fib(n):
    li = [0,1]
    for i in range(2,n):
        a = li[i - 1] + li[i - 2]
        li.append(a)
    print(li[n-1])


if __name__ == "__main__":
    n = int(input())
    fib(n)