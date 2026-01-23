from collections import Counter

n = int(input())
l = list(map(int, input().split()))
c = Counter(l)
c_len = len(c)
avg = n / c_len

ans = []
for value, count in c.items():
    if count > avg:
        ans.append(value)
ans.sort()
print(*ans)