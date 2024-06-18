# 이차원 배열 생성 후 출력
a = int(input())

num = 0
matrix = [[num + i * a + j for j in range(1, 1 + a)] for i in range(a)]

for i in range(a):
    print()
    for j in range(a):
        print(matrix[i][j], end=" ")

"""
바로 출력
a = int(input())

k = []
b = 1

for i in range(a):
    print()
    for j in range(b,b+a):
        print(j, end=' ')
        b += 1
"""
