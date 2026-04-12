n = int(input())
a = list(map(int, input().split()))

avg = sum(a) / n
ans = 0
for i in a:
    if i >= avg:
        ans += 1

print(ans)