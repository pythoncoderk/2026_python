from collections import Counter

s = input()
c = Counter(s)

l = []
for i in s:
    if i not in l:
        print(i, end="")
        print(c[i], end="")

        l.append(i)