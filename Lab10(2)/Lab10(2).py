from random import randint

n = int(input("n = "))
a = [[randint(-20, 20) for j in range(n)] for i in range(n)]
print(a)

f = open('002.txt', "w")

for i in range(n):
    print(a[i][i], file=f)


def replacement(num):
    for i in range(num):
      a[i][i] = 0
    return a


print(replacement(n))
f.close()
