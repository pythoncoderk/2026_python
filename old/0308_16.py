l = list(map(int, input().split()))

l2 = [0] * (len(l) + 1)

for i in range(len(l)):
    l2[i + 1] = l2[i] + l[i]

ans = l2[3] - l2[0]

for i in range(len(l) - 3 + 1):
    ans = max(ans, l2[i + 3] - l2[i])

print(ans)