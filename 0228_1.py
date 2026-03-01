n = int(input())
s = input()

cnt = 0
for i in s:
    if i == "o":
        cnt += 10

print(cnt)