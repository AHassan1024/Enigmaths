
# MT Enigmaths Parser

import math
import array as arr
import datetime
# import numpy as np

print("Welcome to the triangular number generator!")


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


# Idea: All triangular numbers under 1000

triangulars = []
for n in range(1415, 4473):
    trn = (n*n - n)//2
    if (0 not in tolist(trn)):
        triangulars.append(trn)
print(triangulars, len(triangulars))
# print(toint([1, 2, 3])

counter = 0
answerlist = []
answerlist.append(('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', "6A", "ldiag", "rdiag", "1D",
                  "2A", "2D", '3D', '4A', '4D', '5D'))

beg = datetime.datetime.now()
for ldiag in triangulars:
    for rdiag in triangulars:
        for sixA in triangulars:
            if ldiag != rdiag and ldiag != sixA and rdiag != sixA:
                [a, b, c, e, f, j, k] = tolist(ldiag)
                print(ldiag)
                # rdiag = toint([a, c, d, h, i, o, p])
                if (tolist(rdiag)[0] == a) and (tolist(rdiag)[1] == c):
                    [d, h, i, o, p] = tolist(rdiag)[2::]
                    print(d, h, i, o, p)
                    if (a + b + c + d == 15 or a + b + c + d == 21):
                        # We have a, b, c, e, f, j, k
                        # sixA = toint([j, k, l, m, n, o, p])
                        print(a, b, c, d)
                        [l, m, n] = tolist(sixA)[2:5]
                        if (i + n + o + p == 15 or i + n + o + p == 21):
                            print(i, n, o, p)
                            if (tolist(sixA)[0:2] == tolist(ldiag)[5:7]) and (tolist(sixA)[5:7] == tolist(rdiag)[5:7]):
                                if (a != 0 and b != 0 and e != 0):
                                    print("l, r diag:", ldiag, rdiag, sixA)
