from itertools import combinations

l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))
l3 = list(map(int, input().split()))

l = l1 + l2 + l3

for i in range(len(l) + 1):  # 0個〜n個選ぶ
    for j in combinations(l, i):
        print(j)