import math


print("Обчислити відстань від точки (x0, y0) до:")
print("1. заданої точки (x, y)")
print("2. заданої прямої ax + by + c = 0;")
print("3. точки перетину прямих x + by + c = 0 і ax + y + c = 0, де ab ≠ 1.")

try:
	ans = int(input("\n# Make your choice > "))

	if ans == 1:

		x=float(input("x="))
		y=float(input("y="))
		x0=float(input("x0="))
		y0=float(input("y0="))

		L=math.sqrt((math.pow((x-x0), 2))+(math.pow((y-y0), 2)))

		print('L= ',L)

	elif ans == 2:
		print("друга прога")

		a = float(input("a="))
		b = float(input("b="))
		c = float(input("c="))
		x0 = float(input("x0="))
		y0 = float(input("y0="))

		D=(abs(a*x0+b*y0+c))/math.sqrt((math.pow(a, 2))+(math.pow(b, 2)))

		print('D= ',D)

	elif ans == 3:
		print("третя прога")

		a = float(input("a="))
		b = float(input("b="))
		c = float(input("c="))
		x0 = float(input("x0="))
		y0 = float(input("y0="))
		x = float(input("x="))
		y = float(input("y="))

		QR=x+b*y
		ZS=a*x+y
		x=-b*y


		T = math.sqrt((math.pow((x - x0), 2)) + (math.pow((y - y0), 2)))

		print('T= ',T)

	else:
		print("\nNumber is not DEFINED!\nPlease enter 1 or 2")

except ValueError:
	print("Error! Print only Integer numbers!")

	input("\nPress ENTER to exit")