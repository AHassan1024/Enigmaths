
# MT Enigmaths Parser

import math
import array as arr
# import numpy as np

print("Welcome to the triangular number generator!")

# Idea: All triangular numbers under 1000

triangulars = arr.array("i", [])
for n in range(2, 46):
    triangulars.append((n*n - n)//2)

print(triangulars)

squares = arr.array("i", [100, 121, 144, 169, 196,
                          225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841, 900, 961])

for i in triangulars:
    if (i < 100) and (i > 10) and (i % 5 != 0) and (i // 10 != 2):
        print(i)

# 1, 4, 9, 16, 25, 36, 49, 64, 81,
