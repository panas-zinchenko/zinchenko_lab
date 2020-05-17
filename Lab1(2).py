n = int(input("Bведіть n: "))

d1 = n % 10
n = n // 10
d2 = n % 10
n = n // 10
d3 = n % 10
 
print("Сума цифр числа:", d1 + d2 + d3)
