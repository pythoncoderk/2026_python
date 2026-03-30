l = [1, 5, 9, 7, 5, 3, 2, 5, 8, 4]
l2 = [0] * (len(l) + 1)

for i in range(len(l)):
    l2[i + 1] = l2[i] + l[i]

print(l2[7] - l2[2 - 1])

