n, d = map(int, input().split())
l = list(map(int, input().split()))

c = []
for i in range(n):
    l2 = []
    for j in range(n):
        if i != j:
            l2.append(abs(l[j]-l[i]))
    if min(l2) >= d:
        c.append(i+1)
print(len(c))
print(*c)




