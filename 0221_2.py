n, m = map(int, input().split())
l2 = []
for i in range(n):
    x = int(input())
    l = list(map(int, input().split()))
    flag = True
    for j in range(len(l)):

        if l[j] not in l2:
            l2.append(l[j])
            print(l[j])
            flag = False
            break

        if j == len(l)-1:
            print(0)




