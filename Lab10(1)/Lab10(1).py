from random import randint

n = int(input("n = "))
m = int(input("m = "))
b = [[randint(-20, 20) for j in range(m)] for i in range(n)]

print(b)


def division(matrix):
    x = 0
    for i in matrix:
        for j in i:
            if abs(j) >= x:
                x = 0
                x += abs(j)

    return x


f = open('001.txt', "w")

print('Найбільше число по модулю ', division(b))

for i in range(n):
    for j in range(m):
        b[i][j] /= division(b)
        print(b[i][j], end=' ', file=f)
    print(' ', file=f)
f.close()
