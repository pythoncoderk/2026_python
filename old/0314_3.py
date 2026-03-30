h, w, q = map(int, input().split())

l = []
for i in range(h):
    l2 = []
    for j in range(w):
        l2.append(1)
    l.append(l2)

for i in range(q):
    x, y = map(int, input().split())
    total = 0
    if x == 2:
        for k in range(-1, ((len(l)+1) * -1), -1):
            l[k] = [1] * (len(l[k]) - y)
            total += y
    else:
        for k in range(y):

            total += sum(l[-1])

            l.pop()
    print(total)
