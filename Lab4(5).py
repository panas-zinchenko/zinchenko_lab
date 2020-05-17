import random

random.seed()
A = [random.randint(-100, 100) for i in range(30)]
ind_min_el = A.index(min(A))
ind_max_el = A.index(max(A))
tmp = A[ind_min_el + 1:ind_max_el]
if len(tmp) == 0:
    tmp = A[ind_max_el + 1:ind_min_el]
    sum = 0
for t in tmp:
    if t > 0:
        sum += t
print("min:", A[ind_min_el])
print("max:", A[ind_max_el])
print("sum:", sum)