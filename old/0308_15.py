l = [1, 5, 9, 7, 5, 3, 2, 5, 8, 4]
l2 = [0] * (len(l) + 1)

left = 0

for i in range(len(l)):
    l2[i + 1] = l2[i] + l[i]

mx = l2[3] - l2[0]

for i in range(len(l) - 3 + 1):
    mx = max(mx, l2[3 + i] - l2[i])

print(mx)
