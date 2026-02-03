q = int(input())

ans = 0
now = False
for i in range(q):
    x = int(input())
    if x == 1:
        ans += 1
    elif x == 2:
        ans = max(ans - 1, 0)
    else:
        if now:
            now = False
        else:
            now = True
    if now and ans >= 3:
        print("Yes")
    else:
        print("No")