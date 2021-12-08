def feibo(n):	# 给定一个值，作为斐波那契数列的长度。
	"""斐波那契数列"""
	li = [0,1]
	for i in range(2,n):
		a = li[i-1] + li[i-2]
		li.append(a)
	for i in range(n):
		print(li[i])

def huiwen(a):
	# 判断是否为回文
	if a[0] != '#':
		for i in range(len(a) // 2):
			if a[i] == a[len(a) - i - 1]:
				flag = 1
			else:
				flag = 0
				break
		if 1 == flag :
			print("True")
		else:
			print("False")


def wanshu(n):
	# 查找完数
	for i in range(2,n):
		sum = 1
		for j in range(2,i // 2 + 1):
			if i % j == 0:
				sum += j
		if sum == i:
			print("{:d} its fastors are 1 ".format(i),end=" ")
			for j in range(2,int(i / 2) + 1):
				if i % j == 0:
					print(j,end=" ")
			print("\n")
def compare(a,s):
    if ( a > s ):
        too_small()
    elif( a < s ):
        too_big()
    elif( a == s ):
        right()

def right():
    print("正确")

def too_small():
    print("太小")

def too_big():
    print("太大")


if __name__ == "__main__":
	# 输入一段字符判断是否为回文。
	a = list(input())
	huiwen(a)


	print("——————————————————————")
	feibo(10)
	print("——————————————————————")
	n = int(input)   # 输入一个整数 查找从2-该数内的所有完数
	wanshu(n)

	print("——————————————————————")

	b = randrange(0,101,2)
    print(a)
    while(1):
        s = int(input("请输入一个偶数:"))
        compare(b,s)
        if(b == s):     #当猜中时不在循环
            break