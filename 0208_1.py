n = int(input())

a, b = map(int, input().split())


l = []
for i in range(n):
    x, y = map(int, input().split())
    l.append([x, y])

l.sort(key=lambda x: (x[0], x[1]))

flag_1 = True

for i in range(n):
    if l[i][0] > a:
        print(i + 1)
        flag_1 = False
        break
    elif l[i][0] == a:
        if l[i][1] > b:
            print(i + 1)
            flag_1 = False
            break
if flag_1:
    print(len(l)+1)

for i in range(n):
    if l[i][0] < 4:
        l[i][0] += 12
    elif l[i][0] == 4 and l[i][1] == 1:
        l[i][0] += 12

l.sort(key=lambda x: (x[0], x[1]))

if a < 4:
    a += 12
elif a == 4:
    if b == 1:
        a += 12

flag_2 = True

for i in range(n):
    if l[i][0] > a:
        print(i + 1)
        flag_2 = False
        break
    elif l[i][0] == a:
        if l[i][1] > b:
            print(i + 1)
            flag_2 = False
            break

if flag_2:
    print(len(l)+1)