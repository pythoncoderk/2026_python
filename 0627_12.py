n, m = map(int, input().split())

l = []

for i in range(n):
    l2 = input()
    l.append(l2)
flag = True
j = 0
while flag:
    flag = True
    l3 = len(l[0])
    for j in range(l3):
        if l[0][j] == "#":
            flag = False
            break
    if flag:
        l.pop(0)

flag = True
while flag:
    flag = True
    l3 = len(l[0])
    for j in range(l3):
        if l[-1][j] == "#":
            flag = False
            break
    if flag:
        l.pop()


flag = True
while flag:
    flag = True
    l3 = len(l)
    for j in range(l3):
        if l[j][0] == "#":
            flag = False
            break
    if flag:
        for k in range(l3):
            l[k] = l[k][1:]

flag = True
while flag:
    flag = True
    l3 = len(l)
    for j in range(l3):
        if l[j][-1] == "#":
            flag = False
            break
    if flag:
        for k in range(l3):
            l[k] = l[k][:-1]

for j in range(len(l)):
    print(l[j])