n = int(input())
l = [int(input()) for _ in range(n)]

num = 1
dem = l[-1]

for i in range(n-2, -1, -1):
    num, dem = dem, dem * l[i] + num

print(dem, num)