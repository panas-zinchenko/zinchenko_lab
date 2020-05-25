import random

# n = int(input("кількість рядків = "))
# m = int(input("кількість стовпчиків = "))
n = m = 3
matrix = []

for i in range(n):
    row = []
    for j in range(m):
        elem = int(random.uniform(0, 10))
        row.append(elem)
    matrix.append(row)
    print(row)

s = 0

for i in range(n):
    for j in range(m):
        if matrix[i][j] > sum(matrix[j])-matrix[i][j]:
            try:
                numLeft = matrix[i][j - 1]
            except:
                print('число зліва не існує')
            else:
                if matrix[i][j] > matrix[i][j-1]:
                    try:
                        numRight = matrix[i][j + 1]
                    except:
                        print('число справа не існує')
                    else:
                        if matrix[i][j] < numRight:
                            print("особливий", i, j)
