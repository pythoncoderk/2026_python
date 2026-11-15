k = int(input())
l = list(map(int, input().split()))

if 9 not in l:
    print(-1)
    exit(0)

print(min(l))