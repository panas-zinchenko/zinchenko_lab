z = int(input("z = "))
y = int(input("y = "))


def x(coordinate_one, coordinate_two):
    if coordinate_one & coordinate_two < 0:
        return 'Точка знаходиться у третьому квадранті'
    else:
        return 'Точка не знаходиться у третьому квадранті'


print(x(z, y))
