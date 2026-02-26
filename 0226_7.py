import sys
from collections import Counter

data = sys.stdin.buffer.read().split()
n = int(data[0])
A = list(map(int, data[1:1+n]))

prefix = 0
counter = Counter()
counter[0] = 1

ans = 0
for a in A:
    prefix += a
    ans += counter[prefix]
    counter[prefix] += 1

print(ans)