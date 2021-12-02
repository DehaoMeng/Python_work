"""
说明:试编写程序：计算该学生所有科目的总分和平均分（保留一位小数）
"""


if __name__ == "__main__":
    s = "语文：80，数学：85，英语：90，物理：76，化学：92"
    a = s.split("，")
    sum = 0
    for i in range(len(a)):
        s = a[i].split("：")
        sum += int(s[1])
    print("{:.1f}".format(sum))
    print("{:.1f}".format(sum / (i + 1)))