import random


def stvorennya_slovnyka(d):
    slovnyk = {}
    for j in d:
        if j not in slovnyk:
            slovnyk[j] = d.count(j)
    return (slovnyk)


n = int(input("n = "))
list = []
for i in range(n):
    k = random.randint(48, 60)
    list.append(chr(k))
print(list)

s = stvorennya_slovnyka(list)
print(s)

m = 0
for key, value in s.items():
    if value > m:
        m = value
        sumvol = key
print("символ - зустрічається {} " .format(sumvol, m))