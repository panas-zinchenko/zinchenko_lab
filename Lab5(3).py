import random


n = int(input("порядок матриці = "))

matrix = []

for i in range(n):
    row = []
    for j in range(n):
        elem = int(random.uniform(1, 10))
        row.append(elem)
    matrix.append(row)
    print(row)

for i in range(n):
    matrix[i][i] = 0
print(matrix)