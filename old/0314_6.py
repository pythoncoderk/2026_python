n = int(input())

r = 0
l = 0

for i in range(n):
    x, y, z = map(str, input().split())
    x = int(x)
    z = int(z)

    if x == 1:
        if y == "L":
            l += z
        else:
            r += z
    elif x == 2:
        if y == "L":
            l -= z
        else:
            r -= z
    else:
        if y == "L":
            l -= z
            r += z
        else:
            r -= z
            l += z
    if l == r:
        print("=")
    elif l > r:
        print(">")
    else:
        print("<")