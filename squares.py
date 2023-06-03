
# MT Enigmaths Parser

import math


print("Welcome to the x-digit entry sum parser!")

# Idea: n such that n % (sum of digits in n) == 0

# n = int(input("Which n? "))
n = 3

print("Here are all the n-digit entries:")

# Range is : (10^(n-1), 10^n)
start = 10**(n-1)
end = 10**n


def is_square(num):
    return (num == (math.ceil(math.sqrt(num))**2))


squares = []

for entry in range(start, end):
    if (is_square(entry)):
        # for i in range(10):
        #     # check entry * i
        #     multiple = entry * i
        #     if ((multiple) < 1000) and (multiple // 100 % 10 == entry // 10 % 10) and (entry % 10 != 0) and (entry != multiple) and (multiple % 10 != 0):
        #         print(entry, multiple)
        # # 2D is a multiple of 1A
        squares.append(entry)
        # print(entry)

print(squares)

pairs = []
for a in squares:
    # No zeroes:
    if (a % 10 != 0):
        for b in squares:
            if (a != b) and ((a//10) % 10 == (b//10) % 10) and (a+b < (999-346)):
                print(a, b, a+b)
                pairs.append((a, b, a+b))
print("Pairs:", pairs)

# Checking which pairs sum to less than 1000 for possible 3D:
thr_D_list = []
for (x, y, z) in pairs:
    for (x1, y1, z1) in pairs:
        if (x != x1) and (y != y1) and (x1 != y) and (x != y1) and (z + z1 <= 999):
            thrD = z+z1
            thrA = (math.floor(thrD/100)*100) + \
                ((math.floor(y1/100) % 100) * 10) + math.floor(y / 100)
            print("3A:", thrA)

            # 7A: %10 of 1D, 2D, 3D
            sevA = (math.floor(x % 10)*100)+(math.floor(x1 %
                                                        10)*10)+(math.floor(thrD % 10))
            print("7A: ", sevA)

            # 6A
            sixA = (math.floor((x % 100)/10))*10000 + \
                (math.floor((x1 % 100)/10))*1000 + \
                (math.floor((thrD % 100)/10))*100 + \
                (math.floor((y1 % 100)/10))*10 + (math.floor((y % 100)/10))

            # 1D, 2D, 3D, 4D, 5D, 3A, 7A, 6A
            if(is_square(thrA) or is_square(sevA)):
                thr_D_list.append((x, x1, thrD, y1, y, thrA, sevA, sixA))
            # print(z, z1, thrD, x, y, x1, y1)


print("Possible 3Ds (1D, 2D, 3D, 4D, 5D, 3A, 7A, 6A): ", thr_D_list)

# print("So, 7A is [1, 4, 5, 9][1, 4, 5, 9][1, 5, 6], and 3A is [8, 9][1, 2, 3, 4][1, 2, 3, 4]\n 3A can be 841. 7A can be....")
# # Brute force checking all possible 7As:
# sevA_huns = [1, 4, 5, 9]
# sevA_tens = [1, 4, 5, 9]
# sevA_ones = [1, 5, 6]
# # Create the list of possible 7As.
# sevA_list = []
# for h in sevA_huns:
#     for t in sevA_tens:
#         for ones in sevA_ones:
#             poss = h*100+t*10+ones
#             sevA_list.append(poss)
#             if is_square(poss):
#                 print(poss)
# print("List of possible 7As:", sevA_list)

# # Brute force checking all possible 3As:
# thrA_huns = [8, 9]
# thrA_tens = [1, 4, 5, 9]
# thrA_ones = [1, 5, 6]
# # Create the list of possible 3As.
# thrA_list = []
# for h in thrA_huns:
#     for t in thrA_tens:
#         for ones in thrA_ones:
#             poss = h*100+t*10+ones
#             thrA_list.append(poss)
#             if is_square(poss):
#                 print(poss)
# print("List of possible 3As:", thrA_list)

# is_square(900)
