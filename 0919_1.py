a = int(input())
b = int(input())
print("equinox" if a == b else "no")


a = int(input())
print("a" if a == b else "b")

a, b = map(int, input().split())
print("a" if a == b else "b")