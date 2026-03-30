n, m = map(int, input().split())
l = list(map(int, input().split()))

for i in range(n):
    if l[i] < m:
        m = l[i]
        print(1)
    else:
        print(0)