
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
for entry in range(start, end):
    # print(entry)

    # Now, find the digit sum
    temp = entry
    sum = 0
    while (temp > 0):
        sum += temp % 10
        temp = temp // 10
    # print(sum)
    if ((entry % sum) == 0):
        # For ones digit:
        # if ((entry % 10) == 1):
        # For tens digit:
        if (((entry // 10) % 10) == 6):
            # For hundreds digit:
            if ((((entry // 10) // 10) % 10) == 8):
                print(entry)


def is_dig_sum(num):
    sum = 0
    temp = num
    while (temp > 0):
        sum += temp % 10
        temp = temp // 10
    if (num % sum) == 0:
        print("True")
    else:
        print("False")


# is_dig_sum(444)
