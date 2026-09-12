s = input()
x = 0
for i in range(len(s)*2-1):
    if i % 2 == 0:
        print(s[x], end="")
        x += 1
    else:
        print("o", end="")
print()