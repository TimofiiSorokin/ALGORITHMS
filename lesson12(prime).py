# https://www.youtube.com/watch?v=ccVlQIeN0l4&list=PLuhNJgi9DRWUS-nAXaXUNWtFvW2574-Tu&index=12
# Проверка числа на простоту
# Разложение на простые множители

# >>>>>>>>> normal O(N) <<<<<<<<<<<
# def isPrime(n):
#     d = 2
#     while n % d != 0:
#         d += 1
#     return d == n
#
#
# n = int(input())
# print(isPrime(n))


# >>>>>>>>> bed way <<<<<<<<<<<
# n = int(input())
# for i in range(2, n+1):
#     if n % i ==0:
#         print("YES")
#         break
# else:
#     print("NO")

# Проверка на простоту от 1 до 100
# >>>>>>>>> Best way O(N^1/2) <<<<<<<<<<<

def isPrime(n):
    d = 2
    while d * d <= n and n % d != 0:
        d += 1
    return d * d > n


# найти суму всех простых чисел от x до y
x = int(input())
y = int(input())
ans = 0
for i in range(x, y + 1):
    if isPrime(i):
        ans += i
print(ans)
