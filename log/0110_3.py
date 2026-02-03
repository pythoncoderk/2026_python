n = int(input())
l = list(map(int, input().split()))
l2 = []
for i in range(n):
    l2.append([l[i], i+1])

l2.sort(key=lambda x: x[0])

l3 = []

for i in range(3):
    l3.append(l2[i][1])

print(*l3)