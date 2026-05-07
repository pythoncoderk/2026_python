try:
    num = 10 / 0
    print(f"徐算の結果は{num}になります")
except ZeroDivisionError:
    print("0で割ることはできません！")

