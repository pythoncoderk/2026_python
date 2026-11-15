s = input()

c = 0

for i in s:
    if i == "o":
        c += 1

print("even" if c % 2 == 0 else "odd")