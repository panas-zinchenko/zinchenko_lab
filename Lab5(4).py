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

y = []

for i in range(n):
    stroki = 0
    for j in range(m):
        stroki += matrix[i][j]
    y.append(stroki)

print("сума = ", y)


print("----------------------------")

y = []

for i in range(n):
    stroki = 1
    for j in range(m):
        stroki *= matrix[i][j]
    y.append(stroki)

print("добуток = ", y)