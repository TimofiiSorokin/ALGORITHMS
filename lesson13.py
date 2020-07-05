# https://www.youtube.com/watch?v=dO-HQOAUTyA&list=PLuhNJgi9DRWUS-nAXaXUNWtFvW2574-Tu&index=13
# Алгоритм Евклида
# (a, b) = (a - b, b)

def gcd(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b


print(gcd(30, 18))
