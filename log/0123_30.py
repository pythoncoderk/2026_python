from collections import Counter

n = int(input())
l = list(map(int, input().split()))
c = Counter(l)

ans = []
for value, count in c.items():
    ans.append([value, count])

ans.sort()
flag = True
for i in range(len(ans)-1):
    if ans[i][1] > ans[i+1][1]:
        flag = False
        break

if flag:
    print("Yes")
else:
    print("No")