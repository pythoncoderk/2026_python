x, y = map(int, input().split())
print("Yes" if x % 16 == 0 and y % 9 == 0 else "No")