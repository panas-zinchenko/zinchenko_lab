import random

n = int(input("кількість рядків = "))
m = int(input("кількість стовпчиків = "))

matrix = []

for i in range(n):
    row = []
    for j in range(m):
        elem = int(random.uniform(1, 10))
        row.append(elem)
    matrix.append(row)
    print(row)

for i in range(n):
    for j in range(m):
        if matrix[i][j] % 2 == 0:
            matrix[i][j] = matrix[i][j] + 1

print(matrix)