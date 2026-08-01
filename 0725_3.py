from itertools import combinations

n = int(input())
m = int(input())

l = []
x = 1
for i in range(n):
    if i == 0:
        l.append(1)
    else:
        l.append(x * 2)
        x *= 2
ans = []

for r in range(1, len(l) + 1):
    for c in combinations(l, r):
        if sum(c) == m:
            ans.append(c)
# print(ans)
ans3 = list(ans[0])

ans2 = list(set(ans3) ^ set(l))
ans2.sort()
final = []

for i in range(len(ans2)):
    for j in range(len(l)):
        if ans2[i] == l[j]:
            final.append(j+1)
            break
print(*final)

