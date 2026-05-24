l = list(map(str, input().split()))

for i in l:
    if i.isdigit():
        print(int(i) + 1)
    else:
        print(i)