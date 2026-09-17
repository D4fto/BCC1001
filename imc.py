peso = eval(input("Digite o peso: "))
altura = eval(input("Digite a altura: "))

imc = peso / altura ** 2

print(imc)


if imc < 18.5:
    print("abaixo do normal")
elif imc < 25:
    print("normal")
else: 
    print("sobrepeso")