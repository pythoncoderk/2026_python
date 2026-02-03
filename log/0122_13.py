from collections import Counter

n = int(input())
l = list(map(int, input().split()))
c = Counter(l)

m = int(input())
l2 = []
for i in range(m):
    l2.append(int(input()))

for i in range(m):
   print(c[l2[i]])
