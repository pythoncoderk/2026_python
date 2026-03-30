n = int(input())

total = 0

for i in range(n - 1):
    row = list(map(int, input().split()))
    total += sum(row)

print(row)
print(total)