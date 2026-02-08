import sys

MONTH_DAYS = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
YEAR = sum(MONTH_DAYS)

# 累積和 prefix[i] = 1月〜i月の合計日数（i=0..12）
prefix = [0]
for x in MONTH_DAYS:
    prefix.append(prefix[-1] + x)

def day_of_year(m, d):
    return prefix[m-1] + d

def main():
    input = sys.stdin.readline
    N = int(input())
    m0, d0 = map(int, input().split())
    p = day_of_year(m0, d0)

    days = [p]
    for _ in range(N):
        m, d = map(int, input().split())
        days.append(day_of_year(m, d))

    s1 = sorted(days)
    r1 = s1.index(p) + 1

    start = day_of_year(4, 2)
    s2 = sorted(days, key=lambda x: (x - start) % YEAR)
    r2 = s2.index(p) + 1

    print(r1)
    print(r2)

if __name__ == "__main__":
    main()
