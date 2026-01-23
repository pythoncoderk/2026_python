from collections import Counter

n = int(input())
l = list(map(int, input().split()))
c = Counter(l)

d = {}

for value, count in c.items():
    if count not in d:
        d[count] = [value]
    else:
        d[count].append(value)

for value, count in sorted(d.items()):
    print(f"{value}:", *count)

