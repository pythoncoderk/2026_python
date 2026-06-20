n = int(input())

count = {}

for i in range(n):
    x = int(input())
    if x in count:
        count[x] += 1
    else:
        count[x] = 1

best_num = 0
best_count = 0

