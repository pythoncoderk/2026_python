n, m = map(int, input().split())
l = []
l2 = [0] * n

for i in range(n):
    x = input()
    l.append(x)

d = dict(zip(l, l2))

for i in range(m):
    y = input()
    if y in d:
        d[y] += 1

for i in range(n):
    if l[i] in d:
        print(d[l[i]])




