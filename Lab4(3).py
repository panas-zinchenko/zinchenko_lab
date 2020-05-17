import random

arr = []
arrFilter = []

for i in range(10):
    arr.append(int(random.random() * 100))

for i in arr:

    if i % 2 == 0:
        arrFilter.append(i)

print(arr)
print("парні = :", arrFilter)