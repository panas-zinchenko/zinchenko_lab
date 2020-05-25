import random

n = int(input("кількість рядків = "))
m = int(input("кількість стовпчиків = "))

matrix = []

for i in range(n):
    row = []
    for j in range(m):
        elem = int(random.uniform(5, 10))
        row.append(elem)
    matrix.append(row)
    print(row)

for i in range(n):
    for j in range(m):
        if matrix[i][j] == min(matrix[i]):
            if matrix[i][j] == max(matrix[j]):
                print("сідлова точка", i, j)
