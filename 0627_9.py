names = ["田中", "鈴木", "佐藤", "高橋"]
ages = [18, 25, 17, 30]

for name, age in zip(names, ages):
    if age >= 20:
        print(name)