a, b = map(int, input().split())
b *= 100
# print(b / a / a * 100)
print("Yes" if (b / a / a * 100) >= 25 else "No")