n = int(input())
l = list(map(int, input().split()))

x = {}

for i in l:
    if i not in x:
        x[i] = 1
    else:
        x[i] += 1

xxx = max(x.values())

print(n - xxx)

