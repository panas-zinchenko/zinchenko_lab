print(".....|0,   x<=0")
print("f(x)=|x^2, 0<x=<1")
print(".....|x^4, x>1")

x = float(input("x = "))

if x <= 0:
    functionX = 0
    print("перша", functionX)
elif x>0 and x<=1:
    functionX = x**2
    print("друга", functionX)
elif x>1:
    functionX = x**4
    print("третя", functionX)
else:
    print("error")


