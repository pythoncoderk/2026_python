n = int(input())
m = int(input())
l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))

ans = l1[0]
cnt = 0
for i in range(len(l2)):
    x = l2[i]
    if len(l1) <= x + cnt:
        break
    cnt += x
    ans += l1[cnt]

print(ans)