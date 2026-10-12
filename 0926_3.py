n = int(input())
s = input()
c = 0
for i in s:
    if i == "1":
        c += 1
x = (c / n) * 100
xx = int(x * 10) / 10
print(xx)