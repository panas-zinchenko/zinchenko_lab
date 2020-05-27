x = int(input('x='))
n = int(input('n='))


def func():
    su = 0
    a = [i for i in range(0, x+1) if i % 2 == 0]
    for i in a:
        s = n**i
        su += s
    return(su)


print(func())