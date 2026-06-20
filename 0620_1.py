a = int(input())
print(a)
print("Yes" if a >= 0 else "No")

b = int(input())
c = int(input())
if b == c:
    print("DRAW")
elif b > c:
    print("A")
else:
    print("B")

d, e = map(int, input().split())
print(d, e)


f = input()
print(f)

g, h = map(str, input().split())
print(g, h)

i = input()
j = input()
print("Yes" if i >= j else "No")