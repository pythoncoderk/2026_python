names = ["田中", "鈴木", "佐藤"]
scores = [80, 95, 70]

for n, s in zip(names, scores):
    if s >= 80:
        print(f"{n} : {s}")