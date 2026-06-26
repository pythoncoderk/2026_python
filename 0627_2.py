n = int(input())
l = list(map(int, input().split()))

count = 0

for i in range(n):
    for j in range(n):
        if l[i] + l[j] == 11:
            count += 1
            l[i] = 0
            l[j] = 0
print(count)