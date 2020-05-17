import math

a=float(input("a="))
b=float(input("b="))
c=float(input("c="))

p=(a+b+c)/2
S=math.sqrt(p*(p-a)*(p-b)*(p-c))

h1=(2*S)/a
h2=(2*S)/b
h3=(2*S)/c

print('h1= ',h1)
print('h2= ',h2)
print('h3= ',h3)

L1=math.sqrt(a*b*(a+b+c)*(a+b-c))
L2=math.sqrt(b*c*(b+c+a)*(b+c-a))
L3=math.sqrt(a*c*(a+c+b)*(a+c-b))

print('L1= ',L1)
print('L2= ',L2)
print('L3= ',L3)

m1=math.sqrt(2*(math.pow(a, 2))+2*(math.pow(b, 2))-(math.pow(c, 2)))/2
m2=math.sqrt(2*(math.pow(a, 2))+2*(math.pow(c, 2))-(math.pow(b, 2)))/2
m3=math.sqrt(2*(math.pow(c, 2))+2*(math.pow(b, 2))-(math.pow(a, 2)))/2

print('m1= ',m1)
print('m2= ',m2)
print('m3= ',m3)
