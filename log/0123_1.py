from collections import Counter

n = int(input())
a = list(map(int, input().split()))

cnt = Counter(a)

# 回数 → 値のリスト を作る
groups = {}
for value, count in cnt.items():
    if count not in groups:
        groups[count] = []
    groups[count].append(value)

# 出現回数が小さい順に処理
for count in sorted(groups.keys()):
    groups[count].sort()  # 値は昇順
    print(f"{count}:", *groups[count])
