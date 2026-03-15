n, k = map(int, input().split())
l = list(map(int, input().split()))


cnt = []
cnt_abs = []

for i in range(1 << n):
    total = 0
    for j in range(n):
        if i & (1 << j):
            total += l[j]
    cnt.append(total)

for i in range(1 << n):
    cnt_abs.append(abs(cnt[i] - k))

check = 10 ** 18
check_ans = 0

for i in range(1 << n):
    if check > cnt_abs[i]:
        check = cnt_abs[i]
        check_ans = cnt[i]
print(check_ans)


