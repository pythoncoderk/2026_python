a = input()
b = input()
c = input()
l = [a, b, c]
l.sort()

print("Yes" if l[0] == "o" and l[1] == "s" and l[2] == "s" else "No")

d = input()
e = input()
print(d, e)

n = int(input())
f = input()

s = 0
o = 0

for i in f:
    if i == "o":
        o += 1
    elif i == "s":
        s += 1
print("Yes" if o >= n else "No")



a = int(input())
g = input()
c = g.count("SOS")
print("YES" if c >= 1 else "NO")

h = input()
print("Yes" if h == "s" or h == "o" else "No")

