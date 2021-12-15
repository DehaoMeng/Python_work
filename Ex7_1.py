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
    # 每次转向后画笔落笔
    t.pendown()
    t.pencolor(datals[i][3],datals[i][4],datals[i][5])
    t.fd(datals[i][0])
    # 每次画后抬笔
    t.penup()
    if datals[i][1]:
        # 突显有抬笔的动作。
        time.sleep(1)
        t.rt(datals[i][2])

    else:
        # 凸显有抬笔的动作。
        time.sleep(1)
        t.lt(datals[i][2])

        
t.done()
