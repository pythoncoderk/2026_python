n, m = map(int, input().split())
k = int(input())

st = set()

l = [[0] * m for _ in range(n)]

d = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1), (0, 0), (0, 1),
    (1, -1), (1, 0), (1, 1)
]

for i in range(k):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    for dx, dy in d:
        r = dx + x
        c = dy + y
        if r >= 0 and r < n and c >= 0 and c < m:
            st.add((r, c))

print(len(st))