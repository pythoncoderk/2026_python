n, q = map(int, input().split())
l = list(map(int, input().split()))

l2 = []
for i in range(n):
    l2.append(i + 1)

for i in range(q):
    l3 = []
    for j in range(l[i]):
        x = l2.pop(0)
        l3.insert(0, x * -1)
    l2 = l3 + l2

for i in l2:
    print(i)