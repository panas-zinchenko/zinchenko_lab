n = int(input("введіть число n: "))


def factorial(n):
    p = 1

    for i in range(n):
        p = p * (i+1)
    return p


print("y= ", factorial(n*2))

print("---------------------------------------------")

print("y= ", factorial(1+n*2))

print("---------------------------------------------")

print("y= ", factorial(n)*factorial(n+1))