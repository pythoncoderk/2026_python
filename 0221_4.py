import sys

def main():
    input = sys.stdin.readline

    N, Q = map(int, input().split())
    A = list(map(int, input().split()))

    # prefix[i] = A[0] + ... + A[i-1] （長さ N+1）
    prefix = [0] * (N + 1)
    for i in range(N):
        prefix[i + 1] = prefix[i] + A[i]

    out = []
    for _ in range(Q):
        l, r = map(int, input().split())  # 1-indexed
        out.append(str(prefix[r] - prefix[l - 1]))

    print("\n".join(out))

if __name__ == "__main__":
    main()

print(main())