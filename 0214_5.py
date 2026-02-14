n = int(input())

l = []
for _ in range(n):
    l.append(int(input()))

cnt = 0

for _ in range(n):
    if l[_] >= 70:
        cnt += 1

avg = sum(l) / len(l)
cnt_2 = 0
for _ in range(n):
    if l[_] >= avg:
        cnt_2 += 1

print(f"{cnt} {cnt_2}")