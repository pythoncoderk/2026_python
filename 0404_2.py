h, w = map(int, input().split())

for i in range(h):
    for j in range(w):
        if i == 0:
            print("#", end='')
        elif i == h-1:
            print("#", end='')
        else:
            if j != 0 and j != w-1:
                print(".", end='')
            else:
                print("#", end='')

    print()