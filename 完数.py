"""
说明:一个数如果恰好等于它的因子和，这个数就称为“完数”，例如，6的因子为1，2，3,而6=1+2+3，因此6就是“完数”。编程找出100内的所有完数。
"""
if __name__ == "__main__":
    for i in range(2,101):
        sum = 1
        for j in range(2,int(i / 2) + 1):
            if i % j == 0:
                sum += j
        if sum == i:
            print("{:d} its fastors are 1 ".format(i),end=" ")
            for j in range(2,int(i / 2) + 1):
                if i % j == 0:
                    print(j,end=" ")
            print("\n")
