fruits = ["りんご", "みかん", "ぶどう"]
prices = [100, 120, 300]


for f, p in zip(fruits, prices):
    print(f"{f} : {p}円")