from random import randint
n = int(input("n = "))
m = int(input("m = "))
a = [[randint(0, 20) for j in range(m)] for i in range(n)]


def value_min(num):
    b = []
    for i in range(num):
        k = min(a[i])
        b.append(k)
    return b


def value_max(num):
    b = []
    for i in range(num):
        k = max(a[i])
        b.append(k)
    return b


f = open('004.txt', "w")
print('Найменші числа кожного рядка', value_min(n), file=f)
print('Найбільші числа кожного рядка', value_max(n), file=f)
f.close()
print('the program is executed')
