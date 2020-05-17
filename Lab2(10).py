a = int(input("Введіть число a: "))
b = int(input("Введіть число b: "))
c = int(input("Введіть число c: "))

if (a + b > c) and (a + c > b) and (b + c > a):
    print("трикутник існує")
else:
    print("не існує")

x = ((a ** 2) - (b ** 2) - (c ** 2))/(- 2 * b * c)
y = ((b ** 2) - (a ** 2) - (c ** 2))/(- 2 * a * c)
z = ((c ** 2) - (a ** 2) - (b ** 2))/(- 2 * b * a)

if x or y or z == 0:
    print("прямокутний")
elif x and y and z > 0:
    print("гострокутній")
elif x or y or z < 0:
    print("тупокітній")
elif (a + b) <= c:
    print("не існує")
elif (a + c) <= b:
    print("не існує")
elif (c + b) <= a:
    print("не існує")
else:
    print()