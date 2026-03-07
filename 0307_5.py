n, k = map(int, input().split())
l = list(map(int, input().split()))

lef = 0
rig = 1

cnt = 0

while True:
    print(l[lef:rig+1])
    if sum(l[lef:rig+1]) <= k:
        cnt += 1
        rig += 1
    elif rig >= len(l):
        lef += 1
        rig = lef + 1
    else:
        lef += 1
        rig = lef + 1
