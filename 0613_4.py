n = int(input())

l = [int(input()) for _ in range(n)]

l.sort(reverse=True)

for i in l:
    print(i)