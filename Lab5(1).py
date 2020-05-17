import random

a = int(random.uniform(1, 10))

b = []

for i in range(3):
    row = []
    for j in range(3):
        elem = int(random.uniform(1, 10))
        row.append(elem)
    b.append(row)
    print(row)

for i in range(3):
    for j in range(3):
        b = a - (3 * a)
print(b)
