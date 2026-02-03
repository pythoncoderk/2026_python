try:
    x = int(input())
    y = 10 / x
except ZeroDivisionError:
    print("0は不可")
else:
    print("計算結果:", y)
