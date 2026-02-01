n = int(input())
l = list(map(int, input().split()))

cnt = 1
loop_cnt = 1
for i in range(n-1):
    if l[i] == l[i+1]:
        loop_cnt += 1
        cnt = max(cnt, loop_cnt)
    else:
        loop_cnt = 1

print(cnt)
