l = []

for i in range(5):
    x = input()
    l.append(x)

yoko = 5

for i in range(5):
    y = 0
    for j in range(5):
        if l[i][j] == ".":
            y += 1
    yoko = min(yoko, y)
tate = 5
for i in range(5):
    t = 0
    for j in range(5):
        if l[j][i] == ".":
            t += 1
    tate = min(tate, t)
m_n = 5
for i in range(1):
    m = 0
    for j in range(5):
        if l[j][j] == ".":
            m += 1
    m_n = min(m, m_n)

f = 5
fff = 0
ii = l[-1][0]
if ii == ".":
    fff += 1

ii = l[-2][1]
if ii == ".":
    fff += 1

ii = l[-3][2]
if ii == ".":
    fff += 1

ii = l[-4][3]
if ii == ".":
    fff += 1

ii = l[-5][4]
if ii == ".":
    fff += 1

f = min(fff, f)


f_f = list([yoko, tate, m_n, fff])
print(min(f_f))