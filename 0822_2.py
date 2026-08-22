n = int(input())
l = list(map(int, input().split()))

l2 = []


for i in range(n):
    x = l[:i+1]
    y = l[i+1:]

    x_max = sum(x)
    y_max = sum(y)

    final = abs(x_max - y_max)
    l2.append(final)

print(min(l2))
