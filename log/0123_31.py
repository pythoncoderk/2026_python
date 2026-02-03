from collections import Counter

n = int(input())
l = list(map(int, input().split()))
c = Counter(l)

sum = 0
cnt = 0
for value, count in c.items():
    sum += count
    cnt += 1
sum = (sum + cnt - 1) // cnt

ans = 0

for value, count in c.items():
    if sum != count:
        ans += abs(count - sum)

print(ans)