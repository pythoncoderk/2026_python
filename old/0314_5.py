n = int(input())

for i in range(n):
    x, y, z = map(str, input().split())
    x = int(x)
    z = int(z)
    if y == "L":
        x += n
        if x > z:
            print(">")
        elif x == z:
            print("=")
        else:
            print("<")
        n += x
    else:
        z += n
        if x > z:
            print(">")
        elif x == z:
            print("=")
        else:
            print("<")
        n += x