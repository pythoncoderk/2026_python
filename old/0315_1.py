h, w, q = map(int, input().split())

for _ in range(q):
    t, x = map(int, input().split())

    if t == 1:
        print(x * w)
        h -= x

    else:
        print(x * h)
        w -= x
