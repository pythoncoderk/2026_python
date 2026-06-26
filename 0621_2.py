n, x = map(str, input().split())
n = int(n)

count = 0

if x == "A":
    count = 0
elif x == "B":
    count = 1
elif x == "C":
    count = 2
elif x == "D":
    count = 3
elif x == "E":
    count = 4

ans = False
for i in range(n):
    s = input()
    if s[count] == "o":
        ans = True

print("Yes" if ans else "No")

