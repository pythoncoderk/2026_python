from collections import Counter

n = int(input())
l = list(map(int, input().split()))
c = Counter(l)

max_value = max(c.values())

ans = []
for k, v in c.items():
    if v == max_value:
        ans.append(k)

ans.sort()
print(ans[0])