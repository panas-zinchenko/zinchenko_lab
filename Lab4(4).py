import random

k = int(input("Введіть  k =  "))

arr = []
arrFilter = []
# counterMax = counterMin = 0

for i in range(10):
    arr.append(int(random.random() * 100))

# for i in arr:
#     if i > k:
#         counterMax += 1
#
# for i in arr:
#     if i < k:
#         counterMin += 1


def maxMin (k, type, array):

    counter = 0

    for i in array:
        if type == 'max':
            if i > k:
                counter += 1
        elif type == 'min':
            if i < k:
                counter += 1
    return counter


print("\n", arr)
print("\nкількість більших = ", maxMin(k, 'max', arr))
print("кількість менших = ", maxMin(k, 'min', arr))

# print("\nкількість більших = ", counterMax)
# print("кількість менших = ", counterMin)