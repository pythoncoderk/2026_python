try:
    num = 10 / 0
    print(f"徐算の結果は{num}になります")

except (ZeroDivisionError, TypeError, NameError) as e:
    print(f" Exception class: {type(e)}")
    print(f" Exception occured: {e}")


print("ここまで！")