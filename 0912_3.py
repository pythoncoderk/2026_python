n = int(input())

l = list(map(int, input().split()))
ll = [0, 0, 0]

for i in range(n):
    y = l[i] % 1000
    if 1000 - y == 1000:
        continue
    else:
        z = 1000 - y

    xx = z // 100
    yy = z % 100

    xxx = yy

    xxxx = xxx // 10
    yyyy = yy % 10
    ll[0] += xx
    ll[1] += xxxx
    ll[2] += yyyy

print(*ll[::-1])


