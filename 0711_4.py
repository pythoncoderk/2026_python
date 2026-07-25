n = int(input())
l = list(map(int, input().split()))
ans = True
for i in range(n):
    if l[i] >= 0:
        ans = False

print("Yes" if ans else "No")