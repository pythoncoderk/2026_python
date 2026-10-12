
N = 4
W = 9

A = [4, 3, 5, 8]
B = [5, 3, 9, 6]

best = 0

for i in range(N):
    for j in range(i + 1, N):

        # 2個のおかずの体積合計
        volume = B[i] + B[j]

        # 容量内なら、おいしさを比較
        if volume <= W:
            taste = A[i] + A[j]
            best = max(best, taste)

print(best)
