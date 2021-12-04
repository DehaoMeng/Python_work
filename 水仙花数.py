"""
说明:找出所有的水仙花数。水仙花数是指一个3位数，它每一位上的数字的3次幂的和等于它本身
"""
from math import pow
if __name__ == "__main__":
    for i in range(100,1000):
        sum = 0
        for j in range(0,3):
            sum += pow(int(i / pow(10,j)) % 10, 3)
        if sum == i:
            print(i,end=' ')