lado1 = float(input("Insira o primeiro lado: "))
lado2 = float(input("Insira o segundo lado: "))
lado3 = float(input("Insira o terceiro lado: "))

if(lado1 == lado2 and lado2 == lado3):
    print("Equilátero")
elif(lado1 == lado2 or lado1 == lado3 or lado2 == lado3):
    print("Isóceles")
else: 
    print("Escaleno")