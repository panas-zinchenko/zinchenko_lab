from random import randint
a = int(input("Введіть діапазон(мінімальне): "))
b = int(input("Введіть діапазон(максимальне): "))

l = []
y = 1
x = 0

m = int(input("Скільки елементів потрібно в списку: "))

while y <= m:
    l.append(randint(a, b))
    y += 1
print(l)

for i in l:
    if i % 2 == 0:
        x += 1
print(" кількість парних = ", x)

print("------------------------------------------------------")

for i in l:
    if i == 0:
        x += 1
print(" кількість парних = ", x)