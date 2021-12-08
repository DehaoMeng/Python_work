"""
说明:
"""

def shuru(txt):
    with open('sc.txt','a',encoding='utf-8') as fp:
        fp.write(txt)

if __name__ == "__main__":
    with open("sc.txt",'w',encoding='utf-8') as fp:
        fp.write("姓名    语文 数学 英语 \n")
    txt = '''罗恩    23   35   44   
哈利    60   77   68   
赫敏    97   99   89   
马尔福  100  85   90   '''
    shuru(txt)