n, x = map(int, input().split())
a = list(map(int, input().split()))

r = 0
total = 0

for l in range(n):
    while r < n and total < x:
        total += a[r]
        r += 1

    if total >= x:
        print("Yes")
        exit()

    total -= a[l]

print("No")