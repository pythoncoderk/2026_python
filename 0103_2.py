s = input()
cnt2 = 0
l = []
se = set()
while True:

    cnt = int(s)

    ans = 0
    for i in s:
        x = int(i)
        ans += x ** 2
    s = str(ans)
    l.append(s)
    se.add(s)
    if "1" in l:
        print("Yes")
        exit()
    elif len(l) != len(se):
        print("No")
        exit()





