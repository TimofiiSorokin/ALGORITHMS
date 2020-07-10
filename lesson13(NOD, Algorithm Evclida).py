# https://www.youtube.com/watch?v=dO-HQOAUTyA&list=PLuhNJgi9DRWUS-nAXaXUNWtFvW2574-Tu&index=13
# Алгоритм Евклида
# Greatest common divisor (gcd)

# (a, b) = (a - b, b)

# def gcd(a, b):
#     while a != 0 and b != 0:
#         if a > b:
#             a = a % b
#         else:
#             b = b % a
#     return a + b
#
#
# print(gcd(30, 18))


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


print(gcd(30, 18))

# 1/3 + 5/6 = ?

a = 1
b = 3
c = 1
d = 3

a, b = a * d + b * c, b * d

print(a // gcd(a, b), "/", b // gcd(a, b))
