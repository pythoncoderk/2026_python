n = int(input())

l = [int(input()) for _ in range(n)]

for i in range(1, n+1):

    while True:
        if i != l[0]:
            x = l.pop(0)
            l.append(x)
        else:
            l.pop(0)
            break
