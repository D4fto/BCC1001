import math

a = eval(input("Digite o a:"))
b = eval(input("Digite o b:"))
c = eval(input("Digite o c:"))

delta = b**2-4*a*c

x1 = (-b+delta**math.sqrt(delta))/2
x2 = (-b-delta**(1/2))/2

print(f"{x1}\n{x2}")

