n = int(input())
l = list(map(int, input().split()))
l2 = []
for i in range(n-2):
    if l[i] < l[i+1] > l[i+2]:
        l2.append(i)

print(len(l2))

