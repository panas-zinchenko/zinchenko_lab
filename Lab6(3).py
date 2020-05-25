import random
import string


def buildblock(size):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(size))


test = buildblock(10)
print(test)

let_s = let_b = digit_counter = 0

for i in test:
    if 'a' <= i <= 'z':
        let_s += 1
    else:
        if 'A' <= i <= 'Z':
            let_b += 1

for i in test:
    if i.isdigit():
        digit_counter += 1
if digit_counter == 0:
    print("чисел не виявлено")
else:
    print("чисел - ", digit_counter)

print("маленьких літер - ", let_s)
print("великих літер - ", let_b)