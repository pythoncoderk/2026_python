n = int(input())
a = list(map(int, input().split()))

ans = []
for x in a:
    if x % 2 == 0:
        ans.append(x)


ans.sort(reverse=True)
print(ans[0])
