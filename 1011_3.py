
A = [4, 3, 5, 8]
B = [5, 3, 9, 6]
W = 7

best = 0

for i in range(4):
    if B[i] <= W:
        best = max(best, A[i])

print(best)
