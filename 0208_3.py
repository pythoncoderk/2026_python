import sys

input = sys.stdin.readline

MONTH_DAYS = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
YEAR = 0
prefix = [0]

for x in MONTH_DAYS:
    YEAR += x
    prefix.append(prefix[-1] + x)  # prefix[i] = 1月〜i月の合計日数

N = int(input())

m0, d0 = map(int, input().split())
p = prefix[m0 - 1] + d0

days = [p]
for _ in range(N):
    m, d = map(int, input().split())
    days.append(prefix[m - 1] + d)

# 1) 1/1起点
s1 = sorted(days)
r1 = s1.index(p) + 1

# 2) 4/2起点（円環）
start = prefix[4 - 1] + 2  # 4/2 の通し日
s2 = sorted(days, key=lambda x: (x - start) % YEAR)
r2 = s2.index(p) + 1

print(r1)
print(r2)
