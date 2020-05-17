n = int(input("Введіть число "))

d1 = n % 10
n = n // 10
d2 = n % 10
n = n // 10
d3 = n % 10

q=d1%2
w=d2%2
e=d3%2

if q==0 and w==0 and e==0:
    print("цифри числа всі парні")
else :
    print("цифри числа не всі парні")
