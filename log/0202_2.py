n = int(input())
l = list(map(int, input().split()))

ans = []
for i in range(n-1):
    ans.append(abs(l[i] - l[i+1]))

print(max(ans))