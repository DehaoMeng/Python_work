"""
说明:用函数来封装，任意2个数的最大公约数和最小公倍数
"""
def zhanzhuan(a,b):
    m = max(a,b)
    n = min(a,b)
    r = m % n
    while r != 0:
        m = n
        n = r
        r = m % n
    m = max(a,b) * min(a,b) // n
    print("最大公约数为:{},最小公倍数:{}".format(n,m))


def fun(a, b):
    if a < b:
        a, b = b, a
    m = a * b
    n = a % b
    while n != 0:
        a = b
        b = n
        n = a % b
    m //= b
    print("最大公约数为:{}最小公倍数为:{}".format(b,m))


if __name__ == "__main__":
    a = int(input())
    b = int(input())
    zhanzhuan(a,b)
    fun(a,b)