n = int(input("Введіть натуральне число =  "))
m = int(input("Введіть число =  "))
k = 0

if n > 0:

    strN = str(n)
    strM = str(m)

    if strM in strN:
        print('є')
    else:
        print('нема')

else:
    print('введіть натуральне число')