import matplotlib.pyplot as plt
import math

arr_val = dict()
one_triangle_ident = 1
two_triangle_ident = 2
three_triangle_ident = 3


def input_value(identificators):
    for i in range(3):
        arr_val["x" + str(identificators) + str(i+1)] = int(input("введіть " + "x" + str(i+1) + " = "))
        arr_val["y" + str(identificators) + str(i+1)] = int(input("введіть " + "y" + str(i+1) + " = "))


print("Введіть координати вершини 1го трикутника")
input_value(one_triangle_ident)

print("\nВведіть координати вершини 2го трикутника")
input_value(two_triangle_ident)

print("\nВведіть координати вершини 3го трикутника")
input_value(three_triangle_ident)


def length_side(x, y, x1, y1):
    return math.sqrt((x1 - x)**2 + (y1 - y)**2)


# довжини сторін першого трикутника
arr_val['a1'] = length_side(arr_val["x11"], arr_val["y11"], arr_val["x12"], arr_val["y12"])
arr_val['b1'] = length_side(arr_val["x12"], arr_val["y12"], arr_val["x13"], arr_val["y13"])
arr_val['c1'] = length_side(arr_val["x11"], arr_val["y11"], arr_val["x13"], arr_val["y13"])
# довжини сторін другого трикутника
arr_val['a2'] = length_side(arr_val["x21"], arr_val["y21"], arr_val["x22"], arr_val["y22"])
arr_val['b2'] = length_side(arr_val["x22"], arr_val["y22"], arr_val["x23"], arr_val["y23"])
arr_val['c2'] = length_side(arr_val["x21"], arr_val["y21"], arr_val["x23"], arr_val["y23"])
# довжини сторін третього трикутника
arr_val['a3'] = length_side(arr_val["x31"], arr_val["y31"], arr_val["x32"], arr_val["y32"])
arr_val['b3'] = length_side(arr_val["x32"], arr_val["y32"], arr_val["x33"], arr_val["y33"])
arr_val['c3'] = length_side(arr_val["x31"], arr_val["y31"], arr_val["x33"], arr_val["y33"])


def triangles_check(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        result = "трикутник існує"
    else:
        result = "трикутник не існує"
    return result


def conversion(angle):
    return angle*math.pi/180


def perimeter(a, b, c):
    p = (a + b + c) / 2
    return p


def area(a, b, c, p):
    return math.sqrt(p * (p - a) * (p - b) * (p - c))


def max_area(area_1, area_2, area_3):
    if area_1 >= area_3 and area_1 >= area_2:
        max_area_triangle = "У 1го трикутника найбільша площа"
    elif area_2 >= area_1 and area_2 >= area_3:
        max_area_triangle = "У 2го трикутника найбільша площа"
    elif area_3 >= area_1 and area_3 >= area_2:
        max_area_triangle = "У 3го трикутника найбільша площа"
    else:
        max_area_triangle = ''

    result = "\nПлоща 1го = " + str(area_1) + "\n" + "Площа 2го = " + str(area_2) + "\n" + "Площа 3го = " + str(area_3) + "\n" + max_area_triangle
    return result


print("\nперший ", triangles_check(arr_val['a1'], arr_val['b1'], arr_val['c1']))
print("другий ", triangles_check(arr_val['a2'], arr_val['b2'], arr_val['c2']))
print("третій ", triangles_check(arr_val['a3'], arr_val['b3'], arr_val['c3']))

arr_val['area_1'] = area(arr_val['a1'], arr_val['b1'], arr_val['c1'], perimeter(arr_val['a1'], arr_val['b1'], arr_val['c1']))
arr_val['area_2'] = area(arr_val['a2'], arr_val['b2'], arr_val['c2'], perimeter(arr_val['a2'], arr_val['b2'], arr_val['c2']))
arr_val['area_3'] = area(arr_val['a3'], arr_val['b3'], arr_val['c3'], perimeter(arr_val['a3'], arr_val['b3'], arr_val['c3']))

print(max_area(arr_val['area_1'], arr_val['area_2'], arr_val['area_3']))

f = open("data.txt", "w")

print("площа 1го", arr_val['area_1'], file=f)
print("периметр", perimeter(arr_val['a1'], arr_val['b1'], arr_val['c1']), file=f)

print("площа 2го", arr_val['area_2'], file=f)
print("периметр", perimeter(arr_val['a2'], arr_val['b2'], arr_val['c2']), file=f)

print("площа 3го", arr_val['area_3'], file=f)
print("периметр", perimeter(arr_val['a3'], arr_val['b3'], arr_val['c3']), file=f)

f.close()

arr_val['array_1_x'] = [arr_val["x11"], arr_val["x12"], arr_val["x13"], arr_val["x11"]]
arr_val['array_1_y'] = [arr_val["y11"], arr_val["y12"], arr_val["y13"], arr_val["y11"]]

arr_val['array_2_x'] = [arr_val["x21"], arr_val["x22"], arr_val["x23"], arr_val["x21"]]
arr_val['array_2_y'] = [arr_val["y21"], arr_val["y22"], arr_val["y23"], arr_val["y21"]]

arr_val['array_3_x'] = [arr_val["x31"], arr_val["x32"], arr_val["x33"], arr_val["x31"]]
arr_val['array_3_y'] = [arr_val["y31"], arr_val["y32"], arr_val["y33"], arr_val["y31"]]

fig, ax = plt.subplots()

ax.plot(arr_val['array_1_x'], arr_val['array_1_y'], '-', arr_val['array_2_x'], arr_val['array_2_y'], '-', arr_val['array_3_x'], arr_val['array_3_y'], '-')

ax.set(xlabel='x', ylabel='y', title='трикутники')
ax.grid()

fig.savefig("test.png")
plt.show()
