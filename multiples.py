n = 2

start = 10**(n-1)
end = 10**n
counter = 0
for m in range(start, end):
    for o in range(start, end):
        if (m % o == 0):
            if (o % 10 != 0) and (o % 10 != 1) and (o % 10 != 2) and (o % 10 != 5) and (o // 10 % 10 != 1) and (o // 10 % 10 != 2) and (o // 10 % 10 != 5) and (m // 10 % 10 != 1) and (m // 10 % 10 != 2) and (m // 10 % 10 != 5) and (m % 10 != 0) and (m % 10 != 1) and (m % 10 != 2) and (m % 10 != 5) and (m != o):
                counter += 1
                print(m, o)
print(counter)
