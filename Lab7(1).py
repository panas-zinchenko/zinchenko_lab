import math
x = int(input("введіть 1 кут = "))  # в градусах
x1 = int(input("введіть 2 кут = "))  # в градусах
x2 = int(input("введіть 3 кут = "))  # в градусах
x3 = int(input("введіть 4 кут = "))  # в градусах
x4 = int(input("введіть 5 кут = "))  # в градусах
x = x*math.pi/180  # конвертація до радіан
x1 = x1*math.pi/180  # конвертація до радіан
x2 = x2*math.pi/180  # конвертація до радіан
x3 = x3*math.pi/180  # конвертація до радіан
x4 = x4*math.pi/180  # конвертація до радіан
y = math.cos(x)  # відповідь в радіанах
y1 = math.cos(x1)  # відповідь в радіанах
y2 = math.cos(x2)  # відповідь в радіанах
y3 = math.cos(x3)  # відповідь в радіанах
y4 = math.cos(x4)  # відповідь в радіанах
print(y)
print(y1)
print(y2)
print(y3)
print(y4)