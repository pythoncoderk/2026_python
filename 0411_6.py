t, x = map(int, input().split())
l = list(map(int, input().split()))

total = l[0]

for i in range(t+1):
    if abs(l[i] - total) >= x or i == 0:
        print(i, l[i])
        total = l[i]

