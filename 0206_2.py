from datetime import date

a, b = map(int, input().split())
c, d = map(int, input().split())
n = int(input())

xx, yy = 0, 0

cnt = 0
for i in range(n):
    x, y, z = map(int, input().split())
    cnt += z
    if cnt >= n:
        print(x, y)
        xx, yy = str(x).zfill(2), str(y).zfill(2)
        break

xxx = str(a).zfill(2) + str(b).zfill(2)
yyy = str(c).zfill(2) + str(d).zfill(2)



month = int(xxx[:2])
day = int(xxx[2:4])

d = date(2000, month, day)

month2 = int(yyy[:2])
day2 = int(yyy[2:4])
d2 = date(2000, month2, day2)

month3 = int(xx[:2])
day3 = int(yy[:2])

d3 = date(2000, month3, day3)

if abs(d3 - d) == abs(d3 - d2):
    print("DRAW")
elif abs(d3 - d) < abs(d3 - d2):
    print("A")
else:
    print("B")