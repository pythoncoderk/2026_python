n = int(input())

a = [int(input()) for _ in range(n)]

num = 1
den = a[-1]

for i in range(n-2, -1, -1):
    num, den = den, a[i] * den + num

print(den, num)