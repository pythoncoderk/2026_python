n = int(input())
l = list(map(int, input().split()))

l2 = l[int(n/2):]

print(sum(l2))