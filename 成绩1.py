with open("sc1.txt", 'w', encoding='utf-8') as fp:
    # 将表头写入文本文件内
    fp.write("姓名    语文 数学 英语 总分  平均分   不及格门数   班级排名\n")
# 学生的成绩信息
txt = {
    "罗恩": [23, 35, 44],
    "哈利": [60, 77, 68],
    "赫敏": [97, 99, 89],
    "马尔福": [100, 85, 90]
}
for i in txt.values():
    # 获取每位学生的成绩列表
    sum = 0
    s = 0
    # 判断成绩不及格科目的数量以及总成绩
    for j in i:
        if j < 60:
            s += 1
        sum += j
    # 求该生的总分的平均值
    ave = sum / len(i)
    # 精确保留一位小数成绩
    ave = round(ave, 1)
    # 向成绩列表中加入总分和平均分以及不及格门数
    i.append(sum)
    i.append(ave)
    i.append(s)
# 创建一个空列表，存入每位学生的总成绩
q = []
# 循环将每位学生的成绩存入到列表q中
for i in txt.values():
    q.append(i[3])
# 对列表进行排序
q.sort()
for i in txt.values():
    # 循环将每位学生的总成绩和排序后的进行对比
    for j in range(4):
        if q[j] == i[3]:
            # 获取成绩排名，并将名次加入到成绩列表中
            i.append("第{}名".format(j + 1))
# 打开文本文件并追加写入成绩内容
with open("sc1.txt", 'a', encoding='utf-8') as fp:
    # m为学生的姓名，n为学生的成绩列表
    for m, n in txt.items():
        fp.write(m + "    ")
        for i in n:
            fp.write(str(i) + '   ')
        fp.write('\n')


'''
姓名    语文 数学 英语 总分  平均分   不及格门数   班级排名
罗恩    23   35   44   102   34.0   3   第1名   
哈利    60   77   68   205   68.3   0   第2名   
赫敏    97   99   89   285   95.0   0   第4名   
马尔福    100   85   90   275   91.7   0   第3名   
'''