# Enigmaths 205

three_A = [31, 32]
six_A = [11, 12, 14, 16]

# 5A = 3A * 6A
# (1/3/4/5/7)(X)(2)

for a in three_A:
    for b in six_A:
        five_A = a * b
        if (five_A % 10 == 2):
            print(a * b)

print(31*12)

# Answer:
# +=====+
# |14431|
# |83721|
# |12648|
# +=====+
