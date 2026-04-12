H, W = map(int, input().split())
S = input()
grid = [input().strip() for _ in range(H)]

dirs= [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1), (0, 1),
    (1, -1), (1, 0),(1, 1)
]

L = len(S)

for i in range(H):
    for j in range(W):
        for dx, dy in dirs:
            ok = True
            for k in range(L):
                ni = i + dx * k
                nj = j + dy * k

                if not (0 <= ni < H and 0 <= nj < W):
                    ok = False
                    break

                if grid[ni][nj] != S[k]:
                    ok = False
                    break
            if ok:
                print("Yes")
                exit()
print("No")