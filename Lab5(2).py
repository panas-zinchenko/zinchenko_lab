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

max = matrix[0][0]

for i in range(n):
    for j in range(m):
        if matrix[i][j] > max:
            max = matrix[i][j]
print("max = %f " % max)
for i in range(n):
    for j in range(m):
        matrix[i][j] = matrix[i][j] / max
print(matrix)