from collections import Counter

n = int(input())
l = list(map(int, input().split()))
c = Counter(l)

d = {}
for value, count in c.items():
    if count not in d:
        d[count] = 1
    else:
        d[count] += 1

ans = []
for value, count in d.items():
    ans.append([value, count])
ans.sort()

for i in range(len(ans)):
    print(f"{ans[i][0]}:", ans[i][1])