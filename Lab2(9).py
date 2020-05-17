x = int(input("Введіть число x: "))
y = int(input("Введіть число y: "))
z = int(input("Введіть число z: "))

if x != y and x != z and y != z:
    print("3")
elif x != y and x != z and y == z:
    print("2")
elif x == y and x != z and y != z:
    print("2")
elif x != y and x == z and y != z:
    print("2")
elif x == y and x == z and y == z:
    print("0")
else:
    print()


print("------------------------------------")


x = int(input("Введіть число x: "))
y = int(input("Введіть число y: "))
z = int(input("Введіть число z: "))

if x != y and x != z and y != z:
    print("0")
elif x != y and x != z and y == z:
    print("1")
elif x == y and x != z and y != z:
    print("1")
elif x != y and x == z and y != z:
    print("1")
elif x == y and x == z and y == z:
    print("3")
else:
    print()

print("------------------------------------")

