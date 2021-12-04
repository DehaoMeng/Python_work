"""
说明:输入一个字符串，分别统计出其中英文字母、空格、数字和其他字符的个数。
"""
if __name__ == "__main__":
    s = list(input())

    word = 0
    str = 0
    num = 0
    empty = 0
    for i in s:
        if 'a' <= i <= 'z' or 'A' <= i <= 'Z':
            word += 1
        elif '0' <= i <= '9':
            num += 1
        elif i == " ":
            empty += 1
        else:
            str += 1
    print(word, num, empty, str,)