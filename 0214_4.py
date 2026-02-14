h, n = map(int, input().split())

hp = h
mx = h

for i in range(n):
    x, y = input().split()
    y = int(y)

    if x == "damage":
        hp = max(0, hp - y)
    elif x == "heal":
        hp = hp + y
    else:
        if hp > y:
            hp = y
print(hp)