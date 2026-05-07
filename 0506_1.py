x = int(input())

flag = False

for i in range(1, 7):
    for j in range(1, 7):
        for k in range(1, 7):
            if i + j + k == x:
                flag = True
                break

print("Yes" if flag else "No")