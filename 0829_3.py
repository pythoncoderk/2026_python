n = int(input())
l = list(map(int, input().split()))

for i in range(n):
    for j in range(n):
        if l[i] == l[j] and l[i] != 0 and i != j:
            l[i] = 0
            l[j] = 0
            break
print(sum(l))

