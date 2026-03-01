from collections import Counter

s = input()
c = Counter(s)
# print(c)
mx = max(c.values())

mx_l = []

for k, v in c.items():
    if v == mx:
        mx_l.append(k)

for i in s:
    if i not in mx_l:
        print(i, end="")

print()
