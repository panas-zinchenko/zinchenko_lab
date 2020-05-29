import random
n = int(input("n = "))


def x():
    k = 1
    y = [random.randint(1, 12) for i in range(n)]
    for i in y:
        if i % 3 == 0:
            k *= i
    return k


print(x())