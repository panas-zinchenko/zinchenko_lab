def is_(n):
    for i in range(n):
        for j in range(n):
            r = i ** 2 + j ** 2
            if r == n:
                # print(i, j)
                return True
            # оптимізація коду
            if r > n:
                break
    return False


for i in range(1, 10):
    if is_(i):
        print(i)