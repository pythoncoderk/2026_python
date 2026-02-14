n, m = map(int, input().split())

cnt = n

for i in range(m):
    s, get = map(str, input().split())
    get = int(get)
    if s == "add":
        cnt += get
    else:
        cnt = max(0, cnt - get)

print(cnt)