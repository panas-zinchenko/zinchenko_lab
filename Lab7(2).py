from math import sin
x = int(input("введіть діапазон - "))
dx = int(input("введіть крок - "))
for i in range(x):
    for j in range(x):
        y = sin(x)
        x = x + dx
        print("x =", x, " ", "y=", y)