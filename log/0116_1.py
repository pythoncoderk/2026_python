n, c = map(int, input().split())

l = list(map(int, input().split()))
l.sort()

x = int((n + 1) / 2)-1



print(c - l[x] if c - l[x] > 0 else 0)