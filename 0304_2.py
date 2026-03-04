import sys
from collections import defaultdict

def main():
    input = sys.stdin.readline
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    cnt = defaultdict(int)
    cnt[0] = 1  # 累積和0が最初に1回ある（空の前置き）

    s = 0
    ans = 0
    for x in A:
        s += x
        # s - prev = K  => prev = s - K
        ans += cnt[s - K]
        cnt[s] += 1

    print(ans)

if __name__ == "__main__":
    main()