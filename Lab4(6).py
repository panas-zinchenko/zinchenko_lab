from random import randint

a = int(input("Введіть діапазон(мінімальне) = "))
b = int(input("Введіть діапазон(максимальне) ="))
m = int(input("Скільки елементів потрібно в списку: "))
x = int(input("Введіть шукане число "))

l = []
y = 1

while y <= m:

    l.append(randint(a, b))
    y += 1

print(l)

print("--------------------------------------------------------------------")

r = 0

if x in l:
    k = l.index(x)

    for i in l[:k]:
        r += i

    print("Сума чисел до ", x, "=", r)

else:
    print(0)
print("--------------------------------------------------------------------")

n = int(input("n = "))
s = []
sumD = 0
kstD = 0
kst0 = 0
for i in range(n):
    z = float(input("s = "))
    s.append(z)
print(s)
for elem in s:
    if elem > 0:
        sumD += elem
        kstD += 1
    if elem == 0:
        kst0 += 1
kstV = n - kst0 - kstD
print(sumD)
print(kstV)
print(kst0)