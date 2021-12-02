"""
说明:
"""
from random import randrange,randint
from re import match
if __name__ == "__main__":
    checkcode = ''
    while checkcode == '' or match("^(?![0-9]+$)(?![a-zA-Z]+$)[0-9A-Za-z]{4}$", checkcode) == None:
        checkcode = ''
        for i in range(4):
            index = randrange(0, 4)
            if index != i and index + 1 != i:
                checkcode += chr(randint(97, 122))
            elif index + 1 == i:
                checkcode += chr(randint(65, 90))
            else:
                checkcode += str(randint(0, 9))
    print("当前验证码为：", checkcode)
