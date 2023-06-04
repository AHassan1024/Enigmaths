
# MT Enigmaths Parser

import math
import array as arr
import datetime
# import numpy as np

print("Welcome to the triangular number generator!")

# Idea: All triangular numbers under 1000

triangulars = arr.array("i", [])
for n in range(1415, 4473):
    triangulars.append((n*n - n)//2)

print(triangulars)


# squares = arr.array("i", [100, 121, 144, 169, 196,
#                           225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841, 900, 961])

# for i in triangulars:
#     if (i < 100) and (i > 10) and (i % 5 != 0) and (i // 10 != 2):
#         print(i)

# 1, 4, 9, 16, 25, 36, 49, 64, 81,

def tolist(number):
    li = []
    while (number > 0):
        number, remainder = divmod(number, 10)
        li.insert(0, remainder)
    return(li)
# print(tolist(123543))


def toint(li):
    num = 0
    for i in li:

        num = num + i
        num = num * 10
    num = num // 10
    return(num)


# print(toint([1, 2, 3])

counter = 0
answerlist = []
answerlist.append(('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', "6A", "ldiag", "rdiag", "1D",
                  "2A", "2D", '3D', '4A', '4D', '5D'))

beg = datetime.datetime.now()
# I did another set of for loops, this time starting from the triangular numbers, in triangular_from_triangulars.py


for a in range(1, 10):
    for b in range(1, 10):
        for c in range(0, 10):
            for d in range(1, 10):
                if (a + b + c+d == 15 or a+b+c+d == 21):
                    abcd_time = datetime.datetime.now()
                    print("ABCD at", abcd_time - beg, a, b, c, d)
                    for e in range(1, 10):
                        for f in range(0, 10):
                            for g in range(0, 10):
                                for h in range(0, 10):
                                    for i in range(1, 10):
                                        for j in range(1, 10):
                                            for k in range(0, 10):
                                                # ldiag is triangular
                                                ldiag = toint(
                                                    [a, b, c, e, f, j, k])
                                                if (ldiag in triangulars):
                                                    print("ldiag", ldiag)
                                                    for l in range(0, 10):
                                                        if (e+j+k+l == 15 or e+j+k+l == 21):
                                                            ejkl_time = datetime.datetime.now()
                                                            print(
                                                                "EJKL at", ejkl_time - beg, e, j, k, l)
                                                            for m in range(0, 10):
                                                                if (f+h+g+m == 15 or f+h+g+m == 21):
                                                                    fghm_time = datetime.datetime.now()
                                                                    print(
                                                                        "FGHM at", fghm_time - beg, f, g, h, m)
                                                                    for n in range(0, 10):
                                                                        for o in range(0, 10):
                                                                            for p in range(0, 10):
                                                                                if (i+n+o+p == 15 or i+n+o+p == 21):
                                                                                    inop_time = datetime.datetime.now()
                                                                                    print(
                                                                                        "INOP at", inop_time - beg, i, n, o, p)
                                                                                    #rdiag is triangular
                                                                                    rdiag = toint(
                                                                                        [a, c, d, h, i, o, p])
                                                                                    if (rdiag in triangulars):
                                                                                        print(
                                                                                            "rdiag at", datetime.datetime.now() - beg, rdiag)
                                                                                        # sixA is triangular
                                                                                        sixA = toint(
                                                                                            [j, k, l, m, n, o, p])
                                                                                        if (sixA in triangulars):
                                                                                            print(
                                                                                                "sixA at", datetime.datetime.now() - beg, sixA)
                                                                                            print(
                                                                                                a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p)
                                                                                            answerlist.append(
                                                                                                (a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p))


# for sixA in triangulars:
#     if (sixA//1000000 == 1 and (sixA % 10 == 1)) and (0 not in tolist(sixA)):
#         [j, k, l, m, n, o, p] = tolist(sixA)
#         if (m == 8):
#             for rdiag in triangulars:
#                 if (rdiag//1000000 == 1 and (rdiag % 10 == 1)) and (0 not in tolist(rdiag)):
#                     [a, c, d, h, i, o, p] = tolist(rdiag)

#                     for ldiag in triangulars:
#                         if ((ldiag//1000000 == 1) and (ldiag % 10 == 1)) and (0 not in tolist(ldiag)) and (ldiag != rdiag != sixA):
#                             [a, b, c, e, f, j, k] = tolist(ldiag)

#                             if ((a+b+c+d == 15) or (a+b+c+d == 21)) and ((e+j+k+l == 15) or (e+j+k+l == 21)) and ((i+n+o+p == 15) or (i+n+o+p == 21)) and (a == 1) and (c == 7) and (m == 8):
#                                 # g = 21 - f - h  - m
#                                 # When f+g+h+m == 15:
#                                 g = 15 - f - h - m
#                                 if g == 2:
#                                     print("g:", g)
#                                     counter += 1
#                                     # print("Possible gs:", 21-f-h-m, 15-f-h-m)
#                                     # print(sixA, ldiag, rdiag)
#                                     answerlist.append((sixA, ldiag, rdiag))
#                                 g = 21 - f - h - m
#                                 if g == 2:
#                                     print("g:", g)
#                                     counter += 1
#                             # print("Possible gs:", 21-f-h-m, 15-f-h-m)
#                             # print(sixA, ldiag, rdiag)
#                                     answerlist.append(
#                                         (sixA, ldiag, rdiag, toint([a, c, g, m]), toint([b, c, d]), toint([b, f, l]), toint([d, h, n]), toint([e, f, g, h, i]), toint([e, k]), toint([i, o]), a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p))

# print("Num possibilities:", counter)
print(answerlist)
print("Done in", datetime.datetime.now() - beg)
