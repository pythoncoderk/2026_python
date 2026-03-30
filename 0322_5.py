s1, s2 = map(str, input().split())
s3 = input()

s3 = s3.replace(s1, '*')
s3 = s3.replace(s2, '@')

flag = False
i = 0
ans = ""
while i < len(s3):
    if s3[i] == "*":
        flag = True
        i += 1
    if flag:
        print(s3[i], end='')
        ans += s3[i]
        i += 1
    if s3[i] == "@":
        print()
        flag = False
        ans = ""
        i += 1
    if flag == False:
        i += 1
