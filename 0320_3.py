n, m = map(int, input().split())
k = int(input())

dirs = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1), (0, 0), (0, 1),
    (1, -1), (1, 0), (1, 1)
]

st = set()

for _ in range(k):
    r, c = map(int, input().split())
    r -= 1
    c -= 1

    for dr, dc in dirs:
        nr = r + dr
        nc = c + dc
        if 0 <= nr < n and 0 <= nc < m:
            st.add((nr, nc))

print(len(st))