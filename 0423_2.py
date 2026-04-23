n = int(input())
l = list(map(int, input().split()))
cnt = 0
ln = len(l)
while len(l) >= 3:
    if l[0] == 1 and l[1] == 1 and l[2] == 2:
        l.pop(0)
        l.pop(0)
        l.pop(0)
        cnt += 1
    else:
        l.pop(0)

print(cnt)

