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
    print(sum(matrix[i]) / len(matrix[i]))

