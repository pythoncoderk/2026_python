m, n = map(str, input().split())
a, b = map(str, input().split())

aaa = m.zfill(2) + n.zfill(2)
bbb = a.zfill(2) + b.zfill(2)

aaa_int = int(aaa)
bbb_int = int(bbb)

num = int(input())

cnt = 0

ans_a, ans_b = "", ""

for i in range(num):
    get_a, get_b, get_int = map(str, input().split())
    cas_get_int = int(get_int)

    cnt += cas_get_int

    if cnt >= 5:
        print(get_a, get_b)
        ans_a = get_a.zfill(2)
        ans_b = get_b.zfill(2)
        break
    else:
        pass

ans = int(ans_a + ans_b)

final_a = abs(ans - aaa_int)
final_b = abs(ans - bbb_int)

print(final_a, final_b)




