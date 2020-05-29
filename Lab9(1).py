a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))


def triangle(AB, BC, AC):
    if (AC + AB > BC) and (AC + BC > AB) and (AB + BC > AC):

        x = ((AC ** 2) - (AB ** 2) - (BC ** 2)) / (- 2 * AB * BC)
        y = ((AB ** 2) - (AC ** 2) - (BC ** 2)) / (- 2 * AC * BC)
        z = ((BC ** 2) - (AC ** 2) - (AB ** 2)) / (- 2 * AB * AC)

        if x or y or z == 0:
            type_triangle = "Прямокутний"
        elif x and y and z > 0:
            type_triangle = "Гострокутний"
        elif x or y or z < 0:
            type_triangle = "Тупокутний"
        else:
            type_triangle = "Інший тип"

        return "Трикутник існує" + "\n" + "Тип " + type_triangle
    else:
        return "Трикутник не існує"


print(triangle(a, b, c))

