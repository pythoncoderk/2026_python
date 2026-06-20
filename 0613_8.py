n = int(input())

d = {}

for i in range(n):
    x = int(input())
    if x not in d:
        d[x] = 1
    else:
        d[x] += 1

best_num = 0
best_count = 99999999999999999999999999999

for x, y in d.items():
    if best_num < y:
        best_num = x
        if y < best_count:
            best_count = y

print(best_num, best_count)

