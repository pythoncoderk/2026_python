h, w = map(int, input().split())
l = []
for i in range(h):
    x = input()
    l.append(x)
print(l)
ans = 0

for i in range(h):
    for j in range(w):
        for k in range(2, w+1):
            x = l[i]
            y = x[j:k]
