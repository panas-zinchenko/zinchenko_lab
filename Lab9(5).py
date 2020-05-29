L = [22, 54, 666, 43, 42, 53, 23, 11]
r = int(input("число "))
print(L)


def check():
    p = 0

    for i in L:
        if i < r:
            p += 1
    return p


def check_1():
    x = 0
    
    for i in L:
        if i > r:
            x += 1
    return x


print('Кількість чисел менше ніж К - ', check())
print('Кількість чисел більше ніж К - ', check_1())
