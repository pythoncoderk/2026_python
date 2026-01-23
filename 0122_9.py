from collections import Counter

s = input()
c = Counter(s)

max_cnt = max(c.values())

ans = min(ch for ch, cnt in c.items() if cnt == max_cnt)

print(ans)