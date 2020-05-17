import random

arr = []

for i in range(10):
    arr.append(int(random.random() * 100))

print(sorted(arr, key=int))