n = int(input())

x = {}

for i in range(n):
    s = input()
    s1 = s.lower()
    if s1 in x:
        x[s1] += 1
    else:
        x[s1] = 1

print(max(x.values()))




