"""
说明:对用户输入的英文字母串中出现的英文字母进行提取（不区分大小写，重复字母只计一次），并将提取的结果按照字母顺序升序排列后输出。
例如，用户输入”I miss  you”，程序输出”I,m,o,s,u,y” 或”	I,M,O,S,U,Y”
"""
if __name__ == "__main__":
    a = input().lower()
    c = []
    for i in a:
        if i == ' ' or i in c:
            pass
        else:
            c.append(i)
    print('"',end="")
    for i in range(len(c)):
        if i < len(c)-1:
            print(c[i],end=",")
        else:
            print(c[i],end='"')
