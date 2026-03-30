a = [10, 20, 30]
n = len(a)

for bit in range(1 << n):
    chosen = []

    for i in range(n):
        if bit & (1 << i):
            chosen.append(a[i])

    print(chosen)