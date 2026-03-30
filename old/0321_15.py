n, d = map(int, input().split())
l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))

print(l1)
print(l2)

l3 = [0] * (n + 1)
print(l3)

for i in range(n):
    l3[i+1] = l1[i] + l3[i]
total = 0
for i in l2:
    for j in range(1, len(l3)):
        if l3[j] >= i and l3[j+1] < i:
            total += j
            break