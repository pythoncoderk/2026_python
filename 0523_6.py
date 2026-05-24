n = int(input())
s = "HelloWorld"
for i in range(len(s)):
    if i + 1 == n:
        pass
    else:
        print(s[i], end="")
print()