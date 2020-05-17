from random import randint
a = int(input("Введіть діапазон(мінімальне): "))
b = int(input("Введіть діапазон(максимальне): "))

l = []
y = 1

m = int(input("Скільки елементів потрібно в списку: "))

while y <= m:
    l.append(randint(a, b))
    y += 1
print(l)
min(l)
print("l = ", min(l))

print("-------------------------------------------------------------")

while y <= m:
    l.append(randint(abs(a), abs(b)))
    y += 1
print(l)
max(l)
print("l = ", max(l))

print("-------------------------------------------------------------")

while y <= m:
    l.append(randint(a, b))
    y += 2
print(l)
max(l)
print("l = ", max(l))

print("-------------------------------------------------------------")

while y <= m:
    l.append(randint(a, b))
    y -= 2
print(l)
min(l)
print("l = ", min(l))


def function (y, m, type):
    while y <= m:
        l.append(randint(a, b))
        y -= 2