H, W, N = map(int, input().split())

stamps = []
for _ in range(N):
    stamp = [input() for _ in range(H)]
    stamps.append(stamp)

R, C = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(R)]

for i in range(R):          # 配置の各行
    for h in range(H):      # スタンプ内部の各行
        line = ""
        for j in range(C):  # 配置の各列
            stamp_num = B[i][j] - 1
            line += stamps[stamp_num][h]
        print(line)