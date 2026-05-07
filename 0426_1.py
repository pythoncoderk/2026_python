h, w = map(int, input().split())
l = [input() for _ in range(h)]

ans = 0

for h1 in range(h):
    for h2 in range(h1, h):
        for w1 in range(w):
            for w2 in range(w1, w):
                print(h1, h2, w1, w2)

                flag = True
                for i in range(h1, h2 + 1):
                    for j in range(w1, w2 + 1):
                        ni = h1 + h2 - i
                        nj = w1 + w2 - j

                        if l[i][j] != l[ni][nj]:
                            flag = False
                            break

                if flag:
                    ans += 1
print(ans)