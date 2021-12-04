"""
说明:1.	熟练掌握if-elif-else语句。编程实现，某课程的百分制分数mark，将其转换成4级制
（优(>=90)、中(70--90)、及格(60--70)、不及格(<60)）的评定等级grade。即输入百分制成绩，输出其对应的等级。
"""
if __name__ == "__main__":
    mark = float(input())
    if mark >= 90:
        print("优秀")
    elif 70 <= mark < 90:
        print("中等")
    elif 60 <= mark < 70:
        print("及格")
    else :
        print("不及格")
