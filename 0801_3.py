n = int(input())
s = input()
c = 0
for i in range(n):
    if n == 1:
        if s == "x":
            c += 1
            break
    if i == 0:
        if s[i] == "x" and s[i+1] == "x":
            c += 1
    elif i != n - 1:
        if s[i] == "x" and s[i-1] == "x" and s[i+1] == "x":
            c += 1
    else:
        if s[i] == "x" and s[i-1] == "x":
            c += 1
print(c)