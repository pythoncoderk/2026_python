n = int(input())
s = input()
flag = False
for i in range(n):
    if i == 0 and s[i] == "o":
        flag = True

    if flag and s[i] != "o":
        flag = False
        print(s[i], end="")
    else:
        if flag is False:
            print(s[i], end="")



