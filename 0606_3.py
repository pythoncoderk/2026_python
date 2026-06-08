n = int(input())
l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))
ans = True
for i in range(n):
    if l2[l1[i]-1] != i + 1:
        ans = False

print("Yes" if ans else "No")
