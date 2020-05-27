f = open('001.txt', 'w')

k = 1
while k <= 9:
    s = str(k)
    print(s*k, file=f)
    k += 1

f.close()