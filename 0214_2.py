n = int(input())
l = []
for i in range(n):
    l.append(input())

mx = 0
for i in range(n):
    if len(l[i]) > mx:
        mx = len(l[i])

for i in range(n):
    cnt = mx - len(l[i])
    for j in range(cnt//2):
        print(".", end="")
    print(l[i], end="")
    for k in range(cnt//2):
        print(".", end="")
    print("")
