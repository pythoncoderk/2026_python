n = int(input())
a = list(map(int, input().split()))
s = set(a)
a = list(s)
a.sort(reverse=True)

print(a[1])