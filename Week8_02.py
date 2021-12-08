"""
说明:阶乘
"""
def jc(n):
    if n != 0:
        return n * jc(n-1)
    else:
        return 1
if __name__ == "__main__":
    n = int(input())
    print(jc(n))