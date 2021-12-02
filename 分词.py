"""
说明:
"""
import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud
jieba.setLogLevel(jieba.logging.INFO)
if __name__ == "__main__":
    with open("sg.txt", "r", encoding='utf-8') as fp:
        txt = fp.read()
    txt = txt.lower()
    txt = txt.replace(",", " ")
    txt = txt.replace(",", " ")
    txt = jieba.lcut(txt)
    d = {}
    for i in txt:
        if len(i) == 1:
            continue
        else:
            d[i] = d.get(i, 0) + 1
    ls1 = list(d.items())
    ls1.sort(key=lambda x: x[1], reverse=True)
    with open("tj.txt", "w", encoding='utf-8') as fp1:
        for i in range(0,26):
            x, y = ls1[i]
            print("{:<5}{:>2}".format(x, y))
            fp1.write(x+' ')
    with open('tj.txt', 'r', encoding='utf-8') as txt:
        data = txt.read()
    jieba.load_userdict('tj.txt')
    words_list = jieba.lcut(data)
    tokenstr = ' '.join(words_list)
    mywc1 = WordCloud(
        max_font_size=30,
        min_font_size=10,
        font_path='C:/Windows/Fonts/msyh.ttc',
        background_color='blue',
        width=800,
        height=800
    ).generate(tokenstr)
    plt.imshow(mywc1)
    plt.axis('off')
    plt.show()
    mywc1.to_file('2.png')