from random import randint

a = int(input("Введіть діапазон(мінімальне)"))
b = int(input("Введіть діапазон(максимальне)"))

l = []
y = 1
m = int(input("Скільки елементів потрібно в списку: "))

while y <= m:
    l.append(randint(a, b))
    y += 1

l.append(0)

print("№ найменшого = ", l.index(min(l)))
