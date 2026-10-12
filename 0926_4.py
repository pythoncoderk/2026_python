n = int(input())
s = input()

number = s.count("1")
x = number * 1000 // n

print(f"{x // 10}.{x % 10}")