s = input()
ss = input()

if s[0] == 'A':
    if s[1] == "D" or ss[0] == "D":
        print("Yes")
        exit()
elif s[1] == "A":
    if s[0] == "D" or ss[1] == "D":
        print("Yes")
        exit()
elif ss[0] == "A":
    if s[0] == "D" or ss[1] == "D":
        print("Yes")
        exit()
elif ss[1] == "A":
    if ss[0] == "D" or s[1] == "D":
        print("Yes")
        exit()
elif s[0] == 'D':
    if s[1] == "A" or ss[0] == "A":
        print("Yes")
        exit()
elif s[1] == "D":
    if s[0] == "A" or ss[1] == "A":
        print("Yes")
        exit()
elif ss[0] == "D":
    if s[0] == "A" or ss[1] == "A":
        print("Yes")
        exit()
elif ss[1] == "D":
    if ss[0] == "A" or s[1] == "A":
        print("Yes")
        exit()
print("No")



