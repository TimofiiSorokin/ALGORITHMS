# youtube.com/watch?v=nukRz5Wb2g4&list=PLuhNJgi9DRWUS-nAXaXUNWtFvW2574-Tu&index=8
# Генераторы списков

some = 4  # int(input())
A = [[1, 2, 3, 4], [5, 6, 7, 8], [0, 0, 0, 0]]

# for row in A:
#     # for elem in row:
#     #     print(elem, end='')
# print(A[1])

# for row in A:
#     print(' '.join(map(str, row)))

# N = 4
# K = [0] * N
# for i in range(N):
#     K[i] = list(map(int, input().split()))
# print(K)

# N = 3
# K = []
# for i in range(N):
#     K.append(list(map(int, input().split())))
# print(K)

B = [[0 for j in range(10)] for k in range(5)]
B[0][0] = 5
for row in B:
    print(row)

print(len(B))

