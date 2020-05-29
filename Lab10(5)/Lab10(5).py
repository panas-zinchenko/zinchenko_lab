a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


def min_1():
    n = min(a)
    x = a.index(n)
    return x


def max_1():
    m = max(a)
    y = a.index(m)
    return y


suma = 0

f = open('005.txt', "w")

for i in a[min_1()+1:max_1()]:
    suma += i
    print(i, file=f)
print("cума елементів між позиціями min i max - ", suma)
f.close()
