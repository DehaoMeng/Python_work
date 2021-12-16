from random import randrange
def hw(a):
	# 判断是否为回文
	if a[0] != '#':
		for i in range(len(a) // 2):
			if a[i] == a[len(a) - i - 1]:
				flag = 1
			else:
				flag = 0
				break
		if 1 == flag:
			print("True")
		else:
			print("False")


def fb(n):  # 给定一个值，作为斐波那契数列的长度。
	"""斐波那契数列-迭代"""
	li = [0, 1]
	for i in range(2, n):
		a = li[i - 1] + li[i - 2]
		li.append(a)
	for i in range(n):
		print(li[i])


def ws(n):
	# 查找2-n以内的完数
	for i in range(2, n):
		sum = 1
		for j in range(2, i // 2 + 1):
			if i % j == 0:
				sum += j
		if sum == i:
			print("{:d} its fastors are 1 ".format(i), end=" ")
			for j in range(2, int(i / 2) + 1):
				if i % j == 0:
					print(j, end=" ")
			print("\n")


def zz(p, q):
	# 辗转相除法求最大公约数和最小公倍数
	m = max(p, q)
	n = min(p, q)
	r = m % n
	while r != 0:
		m = n
		n = r
		r = m % n
	m = max(p, q) * min(p, q) // n
	print("最大公约数为:{},最小公倍数:{}".format(n, m))


def tq(a):
	"""
	说明:对用户输入的英文字母串中出现的英文字母进行提取（不区分大小写，重复字母只计一次），并将提取的结果按照字母顺序升序排列后输出。
	例如，用户输入”I miss  you”，程序输出”I,m,o,s,u,y” 或”	I,M,O,S,U,Y”
	"""
	c = []
	for i in a:
		if i == ' ' or i in c:
			pass
		else:
			c.append(i)
	print('"', end="")
	for i in range(len(c)):
		if i < len(c) - 1:
			print(c[i], end=",")
		else:
			print(c[i], end='"')
	print("\n")


def compare(a, s):
	# 随机生成数，用户输入进行猜数。
	if a > s:
		print("太小了")
	elif a < s:
		print("太大了")
	elif a == s:
		print("猜中啦")

def cj(score):
	if score >= 90:
		print("优秀")
	elif 70 <= score < 90:
		print("中等")
	elif 60 <= score < 70:
		print("合格")
	else:
		print("不及格")


print("第一个函数")
# 输入一段字符判断是否为回文。
a = list(input("输入一段字符判断是否为回文"))
hw(a)
print("第二个函数")
# 传递给fb函数一个长度，求该长度内的斐波那契数列值
b = int(input("输入一个整数作为斐波那契数列的长度"))
fb(10)
print("第三个函数")
# 输入一个整数 查找从2-该数内的所有完数
c = int(input("输入一个整数查找2到该数内的所有完数"))
ws(c)
print("第四个函数")
# 辗转相除法求两个数的最大公约数和最小公倍数
a = int(input())
b = int(input())
zz(a, b)
print("第五个函数")
# 提取英文字符
a = input("请输入一段英文字符并进行提取单词").lower()
tq(a)
print("第六个函数")
# 随机生成数，用户输入数字猜数
a = randrange(0, 101, 2)
while True:
	s = int(input("请输入一个100以内的数进行猜数游戏"))
	compare(a,s)
	if a == s:
		break
print("第七个函数")
# 判断成绩区间
score = int(input("请输入成绩"))
cj(score)
