h, w, n = map(int, input().split())
l1 = [list(input()) for _ in range(h * n)]
hx, wx = map(int, input().split())
l2 = [list(map(int, input().split())) for _ in range(hx)]

l3 = [[""] * (w * wx) for _ in range(h * hx)]

print(l1)
print(l2)
print(l3)

