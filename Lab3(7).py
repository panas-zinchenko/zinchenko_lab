from random import randint
a = int(input("Введіть діапазон(мінімальне): "))
b = int(input("Введіть діапазон(максимальне): "))

l = []
y = 1
x = 1

m = int(input("Скільки елементів потрібно в списку: "))
p = int(input("Введіть число: "))

while y <= m:
    l.append(randint(a, b))
    y += 1
print(l)
for i in l:
    if i % p == 0:
        x *= i
print("Добуток кратних введеного числа", x)