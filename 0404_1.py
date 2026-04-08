m, d = map(str, input().split())

l = ["17", "33", "55", "77", "99"]
x = m + d

for i in l:
    if x == i:
        print("Yes")
        exit()

print("No")

