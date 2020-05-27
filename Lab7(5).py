def sum(n):
    if n < 9:
        return n
    else:
        return n % 10 + sum(n // 10)


def isLucky(n):
    if n < 100000:
        return False
    else:
        return sum(n % 1000) == sum(n // 1000)


print(isLucky(123321))
print(isLucky(126545))