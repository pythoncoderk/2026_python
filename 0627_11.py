s = input()

e = 0
w = 0

for i in s:
    if i == 'E':
        e = e + 1
    else:
        w = w + 1

print("East" if e > w else "West")