n, m = map(int, input().split())
t = list(input())
a = list(input())

tt = set(t) - set(a)
aa = set(a) - set(t)

i = int(input())

for k in range(i):
    str = list(input())
    t_chk = set(str) & set(tt)
    a_chk = set(str) & set(aa)
    if len(t_chk) != 0 and len(a_chk) == 0:
        print('Takahashi')
    elif len(t_chk) == 0 and len(a_chk) != 0:
        print('Aoki')
    else:
        print('Unknown')



