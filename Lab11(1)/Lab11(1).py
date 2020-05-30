import matplotlib.pyplot as plt
import math


angle1 = int(input("1 кут = "))
angle2 = int(input("2 кут = "))
v10 = int(input("швидкість тіла 1 = "))
v20 = int(input("швидкість тіла 2 = "))
g = 9.8


def conversion(angle):
    return angle*math.pi/180


def max_value(array):
    return round(max(array), 2)


def distance(angle, v):
    return round(v**2 * math.sin(conversion(2 * angle))/g, 2)


def height(angle, v):
    return round(v**2 * (math.sin(conversion(angle))**2)/(2 * g), 2)


def test(angle, v):
    array_x = []
    array_y = []
    test_array = dict()
    data = dict()

    t1 = 0
    t = (2 * v * (math.sin(conversion(angle)))) / g

    while t1 <= t:
        x = v * t1 * math.cos(conversion(angle))
        y = v * t1 * math.sin(conversion(angle)) - (g * t1 ** 2) / 2
        array_x.append(x)
        array_y.append(y)
        data[t1] = str(x) + ", " + str(y)
        t1 += 0.1

    test_array['x'] = array_x
    test_array['y'] = array_y
    test_array['data'] = data

    return test_array


fig, ax = plt.subplots()

graf_1 = test(angle1, v10)
graf_2 = test(angle2, v20)

print("\n-----пошук максимального у та х у-----\n")
print("перший масив")
print("max x >> ", max_value(graf_1['x']))
print("max y >> ", max_value(graf_1['y']))
print("\nдругий масив")
print("max x >> ", max_value(graf_2['x']))
print("max y >> ", max_value(graf_2['y']))

print("\n-----пошук максимального у та х у, за допомогою фізичних рівнянь.-----\n")
print("перший масив")
print("довжина >> ", distance(angle1, v10))
print("висота >> ", height(angle1, v10))
print("\nдругий масив")
print("довжина >> ", distance(angle2, v20))
print("висота >> ", height(angle2, v20))

data = open("data.txt", "w")

print(graf_1['data'], file=data)
print(graf_2['data'], file=data)

data.close()

ax.plot(graf_1['x'], graf_1['y'], '-', graf_2['x'], graf_2['y'], '.')

ax.set(xlabel='довжина', ylabel='висота', title='траєкторія руху тіл')
ax.grid()

fig.savefig("test.png")
plt.show()
