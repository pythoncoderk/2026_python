from collections import Counter

n = int(input())
l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))
c1 = Counter(l1)
c2 = Counter(l2)

mx1 = max(c1.values())
mx2 = max(c2.values())

ans = [mx1, mx2]
ans.sort()

print(*ans)