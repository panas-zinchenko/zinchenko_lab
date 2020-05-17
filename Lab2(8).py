x=float(input("Введіть число x: "))
y=float(input("Введіть число y: "))
z=float(input("Введіть число z: "))

print("----------------------------------------")

arrAbs = [abs(x), abs(y), abs(z)]

print(arrAbs)
print("\nMin > ", min(arrAbs))
print("Max >", max(arrAbs))

print("----------------------------------------")

el1 = x+y+z
el2 = x*y - x*z + y*z
el3 = x*y*z

arrSum = [el1, el2, el3]

print(arrSum)
print("\nMin > ", min(arrSum))
print("Max > ", max(arrSum))

print("----------------------------------------")

el4 = x*y
el5 = x*z
el6 = y*z

arrSum2 = [el4, el5, el6]

print(arrSum2)
print("\nMin > ", min(arrSum2))
print("Max > ", max(arrSum2))


