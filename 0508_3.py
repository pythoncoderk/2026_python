try:
    num = 10 / '2'

except ZeroDivisionError:
    print("0で割れない")

except TypeError:
    print("文字列は不可")