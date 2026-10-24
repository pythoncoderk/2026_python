n, k = map(int, input().split())
l = list(map(int, input().split()))

c = 0

for i in range(n-1):

    if i == 0:
        if l[i] == k:
            c += 1
            continue

    if l[i] > k and l[i+1] <= k:
        c += 1
    elif l[i] < k and l[i+1] >= k:
        c += 1
    elif l[i] == k and l[i+1] == k:
        c += 1


print(c)