numero = 0
soma = 0

while (numero >= 0):
  soma += numero
  numero = eval(input("Digite outro número: "))

print(f"A soma é {soma}")