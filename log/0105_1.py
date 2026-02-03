n = int(input())
words = input().split()
s = "".join(words)

target = "paiza"
j = 0
ans = 0

for ch in s:
    if ch == target[j]:
        j += 1
        if j == 5:
            ans += 1
            j = 0

print(ans)