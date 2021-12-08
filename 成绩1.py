"""
说明:
"""

if __name__ == "__main__":
    with open("sc1.txt",'w',encoding='utf-8') as fp:
        fp.write("姓名    语文 数学 英语 总分  平均分   不及格门数   班级排名\n")
    txt = {
        "罗恩":[23, 35, 44],
        "哈利":[60, 77, 68],
        "赫敏":[97, 99, 89],
        "马尔福":[100, 85, 90]
    }
    for i in txt.values():
        sum = 0
        s = 0
        for j in i:
            if j < 60:
                s += 1
            sum += j
        ave = sum / len(i)
        ave = round(ave,1)
        i.append(sum)
        i.append(ave)
        i.append(s)
    q = []
    for i in txt.values():
        q.append(i[3])
    q.sort()
    # print(q)
    for i in txt.values():
        for j in range(4):
            if q[j] == i[3]:
                i.append("第{}名".format(j+1))
    with open("sc1.txt",'a',encoding='utf-8') as fp:
        for m,n in txt.items():
            fp.write(m+"    ")
            for i in n:
                fp.write(str(i)+'   ')
            fp.write('\n')