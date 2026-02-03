import builtins

builtins.print()

ranking = {
    "A":100,
    "B":85,
    "C":95
}

x = ranking.get("A")
print(x)

# for key in ranking:
#     print(key)

print(sorted(ranking, key=ranking.get, reverse=True))
