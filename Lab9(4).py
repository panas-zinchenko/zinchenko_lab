x = input("число = ")
y = int(input("цифра = "))
q = []

for i in x:
    q.append(i)


def check_number(array, num, whole_number):
    for element in array:
        if num == int(element):
            return 'Цифра ' + str(num) + ' входить до числа ' + whole_number
    return 'Цифра ' + str(num) + ' не входить до числа ' + whole_number


print(check_number(q, y, x))
