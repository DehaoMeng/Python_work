# Ex7_1.py
# 导入包
import time
import turtle as t


# 设置画笔格式
t.title('自动轨迹绘制')
t.setup(800, 600, 0, 0)
t.pencolor("red")
t.pensize(5)
t.penup()

# 数据读取
datals = []
f = open("data.txt")
for line in f:
    line = line.replace("\n","")
    datals.append(list(map(eval, line.split(","))))
f.close()

# 自动绘制
for i in range(len(datals)):
    # 判断是为抬笔或者落笔
    if datals[i][0] == 1:
        t.pendown()
    elif datals[i][0] == 0:
        t.penup()
        continue
    t.pencolor(datals[i][4],datals[i][5],datals[i][6])
    t.fd(datals[i][1])
    if datals[i][2]:
        t.rt(datals[i][3])
    else:
        t.lt(datals[i][3])
t.done()
