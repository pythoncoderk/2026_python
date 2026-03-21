n, m = map(int, input().split())
k = int(input())

st = set()

for _ in range(k):
    r, c = map(int, input().split())
    r -= 1
    c -= 1

    for dr in (-1, 0, 1):
        nr = r + dr
        