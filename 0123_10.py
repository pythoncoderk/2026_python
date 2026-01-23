from collections import Counter

n = int(input())
l = list(map(int, input().split()))
c = Counter(l)

m = int(input())

for i in range(m):
    x = int(input())
    print(c[x])