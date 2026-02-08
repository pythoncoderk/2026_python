a, b = map(int, input().split())
c, d = map(int, input().split())

n = int(input())

cnt = 0
flag = False
ans_m, ans_b = 0, 0

for i in range(n):
    x, y, z = map(int, input().split())
    cnt += z
    if cnt >= 5 and not flag:
        ans_m = x
        ans_b = y
        print(x, y)
        flag = True

if a == 4:
    b += 31

if c == 4:
    d += 31

if ans_m == 4:
    ans_b += 31

final_a = abs(ans_b - b)
final_d = abs(ans_b - d)

if final_a == final_d:
    print("DRAW")
elif final_a < final_d:
    print("A")
else:
    print("B")
