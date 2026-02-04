import builtins
import collections
import os
import sys

import lesson_package

import cofig

print(lesson_package.__file__)

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
