"""
说明:
"""
if __name__ == "__main__":
    money = float(input())
    status = input()
    if status == "会员":
        if money >= 100:
            print("{:.2f}".format(money * 0.8))
        else:
            print("{:.2f}".format(money * 0.85))
    elif status == "非会员":
        if money >= 100:
            print("{:.2f}".format(money * 0.85))
        else:
            print("{:.2f}".format(money * 0.9))