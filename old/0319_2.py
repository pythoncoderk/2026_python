n, h, w = map(int, input().split())
sy, sx = map(int, input().split())
s = input()

sy -= 1
sx -= 1

l = []
for i in range(h):
    l2 = list(map(int, input().split()))
    l.append(l2)

for i in s:
    if i == "F":
        sy -= 1
    if i == "B":
        sy += 1
    if i == "L":
        sx -= 1
    if i == "R":
        sx += 1
    print(l[sy][sx])





