
# MT Enigmaths Parser

import math
import array as arr

# n = int(input("Which n? "))
n = 3

# Range is : (10^(n-1), 10^n)
start = 10**(n-1)
end = 10**n

# primes in range [10, 100] =
primes = arr.array("i", [])
for p in range(start, end):
    is_prime = True
    for d in range(2, p):
        if (p % d == 0):
            is_prime = False
    if is_prime:
        if (p % 10 != 0) and (p // 10 % 10 == 8):
            primes.append(p)

print(primes)

print("Here are all the n-digit entries:")

# Range is : (10^(n-1), 10^n)
start = 10**(n-1)
end = 10**n
# for fiveD in range(start, end):
#     for i in primes:
#         if (fiveD % i == 0):
#             fiveD_ten = fiveD // 10 % 10
#             i_one = i % 10
#             if (fiveD_ten == i_one):
#                 if (fiveD % 10 == 3) or (fiveD % 10 == 5):
#                     # print(fiveD, i)
#                     r = 1
