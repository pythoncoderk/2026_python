n = int(input())
l = list(map(int, input().split()))
c = 1
d = 0
g = True
while len(l) >= 1:
    ii = 1
    l2 = l[:10]
    counter = len(l2)
    for i in range(1 + d * 10, c * 10):
        if len(l2) == ii:
            break
        if i not in l2:
            g = False
        ii += 1
    l = l[10:]
    c += 1
    d += 1

print("Yes" if g else "No")
