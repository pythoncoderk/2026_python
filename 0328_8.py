import bisect

n = int(input())
l = []
mx = 0
for i in range(n):
    x, y = map(int, input().split())
    if x == 1:
        l.append(y)
        print(len(l))
    else:
        mx = y
        l.sort()
        b = bisect.bisect_left(l, mx)
        if b == len(l):
            l = []
        else:
            if b == 0:
                pass
            else:
                l = l[:b]
        print(len(l))



