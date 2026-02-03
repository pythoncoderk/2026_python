from collections import Counter

s = input()
c = Counter(s)

ans = []
for value, count in c.items():
    ans.append([value, count])

ans.sort()
for i in range(len(ans)):
    print(ans[i][0], ans[i][1])