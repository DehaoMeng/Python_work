"""
说明:
"""
import time
def fenli(txt):
    linewidth = 60

    plist = "，。！？：；,.!?:;\n"
    for p in plist:
        txt = txt.replace(p, " ")
    newlines = txt.split(" ")

    for newline in newlines:
        print(newline.center(linewidth, " "))
        time.sleep(5)
if __name__ == "__main__":
    txt = '''阳关引,寇凖,
    塞草烟光阔，渭水波声咽。春朝雨霁轻尘歇。
    征鞍发。指青青杨柳，又是轻攀折。
    动黯然，知有后会甚时节。更尽一杯酒，歌一阕。
    叹人生，最难欢聚易离别。且莫辞沉醉，听取阳关彻。
    念故人，千里自此共明月'''
    fenli(txt)

