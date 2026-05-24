n = int(input())
s = list(map(str, input().split()))

s1 = ["a", "b", "c"]
s2 = ["d", "e", "f"]
s3 = ["g", "h", "i"]
s4 = ["j", "k", "l"]
s5 = ["m", "n", "o"]
s6 = ["p", "q", "r", "s"]
s7 = ["t", "u", "v"]
s8 = ["w", "x", "y", "z"]

for i in range(n):
    x = s[i]
    if x[0] in s1:
        print(2, end="")
    elif x[0] in s2:
        print(3, end="")
    elif x[0] in s3:
        print(4, end="")
    elif x[0] in s4:
        print(5, end="")
    elif x[0] in s5:
        print(6, end="")
    elif x[0] in s6:
        print(7, end="")
    elif x[0] in s7:
        print(8, end="")
    elif x[0] in s8:
        print(9, end="")
print()

