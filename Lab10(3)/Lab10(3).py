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


def arithmetic_mean(num):
    k = dict()
    for i in range(num):
        key = i + 1
        k[key] = sum(matrix[i]) / len(matrix[i])
    return k


f = open('003.txt', "w")
print(arithmetic_mean(n), file=f)
f.close()
