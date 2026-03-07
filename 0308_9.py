n, k = map(int, input().split())
l = list(map(int, input().split()))

l2 = [0] * (len(l) + 1)

for i in range(len(l)):
    l2[i + 1] = l2[i] + l[i]

print(l2[k+1] - l2[n])
