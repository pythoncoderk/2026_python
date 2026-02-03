n = int(input())
l = list(map(int, input().split()))

s_l = set(l)
l2 = list(s_l)
l2.sort()

l3 = []

for i in range(len(l2)):
    x = 0
    for j in l:
        if l2[i] == j:
            x += 1
    l3.append(x)

min_l3 = max(l3)

for x in range(len(l3)):
    if l3[x] == min_l3:
        print(l2[x])
        break