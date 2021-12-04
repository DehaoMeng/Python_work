"""
说明:恺撒密码是古罗马恺撒大帝用来对军事情报进行加密的算法，它采用了替换方法对信息中的每一个英文字符循环替换为字母表序列该字符后面第三个字符
"""
if __name__ == "__main__":
    ls = input()
    for i in ls:
        if 'a' <= i <= 'w' or 'A' <= i <= 'W':
            i = ord(i) + 3
            print(chr(i), end='')
        elif 'w' < i <= 'z':
            i = ord(i) - 120 + 97
            print(chr(i), end='')
        elif 'W' < i <= 'Z':
            i = ord(i) - 89 + 65
            print(i)
            print(chr(i), end='')
        else:
            print(i,end='')