# MT Enigmaths Parser

import math


print("Welcome to the [1..49] parser!")

# Idea: n = 10a + b

for n in range(1, 50):
    a = int(n // 10)
    b = n % 10
    # print(n)

    # Creating a flag to check if a number is 'special'
    special = False

    # If n is a cube, set special as True
    if (int(round(n ** (1. / 3)) ** 3) == n):
        special = True
        print("Cube: ", n)

    # If n is a square, set special as True
    if (int(round(n ** (1. / 2)) ** 2) == n):
        special = True
        print("Square: ", n)

    # If n is a prime, set special as True
    # Creating a flag to check if a number has a 'factor'
    factor = False
    if n > 1:
        # Checking for factors
        for i in range(2, 1 + int(round((n + 1) ** (1. / 2)))):
            if (n % i) == 0 and not factor:
                # If factor is found, set factor to True
                factor = True
        # Have parsed through all possible factor-pairs
        if not factor:
            # No factors were found
            special = True
            print("Prime: ", n)

    # If n is a triangular, set special as True
    # Drawing on: Tf = (f)(f+1) / 2
    f = int(math.floor((2 * n) ** (1. / 2)))
    if ((f * (f + 1) // 2) == n):
        special = True
        print("Triangular: ", n)

    # If a number falls outside of the above categories and is divisible by the sum of its digits, it is 'friendly'
    if not special and not (n % (a+b)):
        special = True
        print("Friendly: ", n)

    # Identifying un-labelled cells, or 'others'
    if not special:
        print("Other: ", n)

# Useful for identifying pairs
for n in range(1, 25):
    # Keep adding to this list to check what pairs are left
    if n not in [1]:
        print(n, 50-n)
