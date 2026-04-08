a = int(input())
b = int(input())
print(a if a + b == 10 else a + b)


c, d = map(int, input().split())
print(c if c + d == 10 else c + d)


e = input()

print(False if e == "True" else True)

g, h = map(str, input().split())
print(g if g + h == 10 else g + h)