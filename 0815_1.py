a, b = map(int, input().split())

if a + b == 9:
    print("Nine")
    exit()
if a - b == 9:
    print("Nine")
    exit()
if a * b == 9:
    print("Nine")
    exit()
if a / b == 9:
    print("Nine")
    exit()
print("Nein")