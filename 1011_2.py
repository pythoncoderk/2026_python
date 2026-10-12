n = int(input())
s = input()

rr = 0
rm = 0
rf = 0
for i in range(n):
    if s[i] == "R":
        rr += 1
    else:
        rr = 0
    rf = max(rf, rr)

print(rf)

