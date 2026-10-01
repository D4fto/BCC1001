"""
def boasVindas():
    nome = input("Insira seu nome: ")
    sobrenome = input("Insira seu sobrenome: ")

    print(f"Boas vindas, {nome} {sobrenome}!")

boasVindas()
"""

"""
def calculadora(num1, num2):
    print(f"{num1} + {num2} = {num1 + num2}")
    print(f"{num1} - {num2} = {num1 - num2}")
    print(f"{num1} * {num2} = {num1 * num2}")
    print(f"{num1} / {num2} = {num1 / num2}")

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

calculadora(8.0, 2.0)
"""

"""
def mediaNotas(nota1, nota2, nota3, peso1, peso2, peso3):
    return (nota1 * peso1 + nota2 * peso2 + nota3 * peso3) / (peso1 + peso2 + peso3)

n1 = float(input("Insira a primeira nota: "))
p1 = float(input("Insira o primeiro peso: "))
n2 = float(input("Insira a segunda nota: "))
p2 = float(input("Insira o segundo peso: "))
n3 = float(input("Insira a terceira nota: "))
p3 = float(input("Insira o terceiro peso: "))

media = mediaNotas(n1, n2, n3, p1, p2, p3)

print(f"A média é {media}")

"""

def hipotenusa(cateto1, cateto2):
    somaQuadradoCatetos = cateto1**2+cateto2**2
    hip = somaQuadradoCatetos**(1/2)
    return hip

cat1 = eval(input("Insira o primeiro cateto: "))
cat2 = eval(input("Insira o segundo cateto: "))

print(f"A hipotenusa é {hipotenusa(cat1, cat2)}")