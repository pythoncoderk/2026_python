n = int(input())
m = int(input())

c = format(m, f"0{n}b")[::-1]

l = []
for i in range(n):
    if c[i] == "0":
        l.append(i+1)
print(*l)