l = [1, 5, 9, 7, 5, 3, 2, 5, 8, 4]
l2 = [0] * (len(l) + 1)
l3 = [0] * (len(l) + 1)

for i in range(len(l)):
    if l[i] % 2 == 0:
        l2[i + 1] = 0
    else:
        l2[i + 1] = 1

for i in range(len(l)+1):
    l3[i] = l2[i - 1] + l2[i]