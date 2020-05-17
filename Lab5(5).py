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


min_mx = 100

for i in range(n):
    min_i = min(matrix[i])
    if min_i < min_mx:
        min_mx = min_i
print("мінімум = ", min_mx)

for i in range(n):
    for j in range(m):
        if min_mx == matrix[i][j]:
            print('Row: %d, col: %d' % (i+1, j+1))

max_mx = 100

for i in range(n):
    max_i = max(matrix[i])
    if max_i < max_mx:
        max_mx = max_i
print("максимум = ", max_mx)

for i in range(n):
    for j in range(m):
        if max_mx == matrix[i][j]:
            print('Row: %d, col: %d' % (i+1, j+1))
