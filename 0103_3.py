n = int(input())
s = input()

char = "paiza"
cnt = 0

final_cnt = 0

ans = ""
for i in s:
    cnt = cnt % 5
    st = char[cnt]
    if st == i:
        ans += i
        cnt += 1
    if ans == "paiza":
        ans = ""
        final_cnt += 1
print(final_cnt)

