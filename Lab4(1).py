n = int(input("Введіть  n =  "))

arr = []
arrFactorial = []


def factorial(num):
    p = 1

    for i in range(num):
        p = p * (i+1)
    return p


for i in range(n):
    arr.append(str(i + 1) + '!')
    arrFactorial.append(factorial(i + 1))

print("\n", arr, "\n")
print(arrFactorial)