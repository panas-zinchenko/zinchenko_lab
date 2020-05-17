n = int(input("Введіть число n: "))

if n == 0:
    print('введіть число відмінне від нуля')
else:
    string = ''

    for i in range(0, n):
        string = string + "*" + str(i+1)

    # видаляємо 1й символ у рядку
    print("n! = ", string[1:])