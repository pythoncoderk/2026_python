n = int(input())
l = list(map(str, input().split()))

mx = 0
for i in range(n):
    mx = max(len(l[i]), mx)

mi = 100000000000000000
for i in range(n):
    mi = min(len(l[i]), mi)

print(mx - mi)

