numbers = [10, 25, 30, 17, 40]

for i, n in enumerate(numbers):
    if i % 2 == 0 and i != 0:
        print(f"{i} : {n}")