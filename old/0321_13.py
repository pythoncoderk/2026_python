n = int(input())

for i in range(n, 0, -1):
    if i != 1:
        print(i, end=',')
    else:
        print(i)
