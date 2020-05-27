def finedSymb(c):
    sum = 0
    for row in f:
        g = len(row)
        print(g)
        if row[g-2] == c:
            sum += 1
    return sum


n = int(input("введіть кількість рядків у файлі - "))
f_name = input("задайте ім'я файлу - ")
f = open(f_name, "w")
k = 1

while k <= n:
    s = input("введіть дані для рядка файлу - ")
    print(s, file=f)
    k += 1
f.close()
b = input("який символ шукати: ")
f = open(f_name)
print("sum=%d" % finedSymb(b))
f.close()