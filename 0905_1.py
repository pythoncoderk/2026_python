n = int(input())
s = input()
l = []
dx = s[:4]
ex = s[5:7]
fx = s[8:]

total = int(dx + ex + fx)


fff = int(dx + ex + fx)
for i in range(n):
    y = s
    x = list(map(str, input().split()))
    a = x[0]
    b = x[1]

    d = b[:4]
    e = b[5:7]
    f = b[8:]
    g = int(d + e + f)

    front = int(dx + ex + fx)
    if  g >= total:
        l.append([a, b])


if len(l) > 0:
    for a in l:
        print(*a)
else:
    print("NoResults")



