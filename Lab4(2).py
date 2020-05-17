import random

arr = []

for i in range(10):
    arr.append(int(random.random() * 100))

print(arr)

even = 0

for i in arr:

    if i % 2 == 0:
        even += 1

print("парні = :", even)

print("------------------------------------------")


def isPrime(n):
    d = 2
    while d * d <= n and n % d != 0:
        d += 1
    return d * d > n


counter = 0

for i in arr:
    if isPrime(i):
        counter += 1



print("простих чисел = ", counter)


