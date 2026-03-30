n, k = map(int, input().split())
l = list(map(int, input().split()))

total_l = []
total_ans = []

for i in range(1 << n):
    total = 0
    for j in range(n):
        if i & (1 << j):
            total += l[j]
    total_l.append(abs(total - k))
    total_ans.append(total)

mi_total = min(total_l)
final = []
for i in range(len(total_ans)):
    if mi_total == total_l[i]:
        final.append(total_ans[i])
print(min(final))
