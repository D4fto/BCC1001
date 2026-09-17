qtd = eval(input("Quantidade de numeros para média: "))

lista = []

for i in range(qtd):
    lista.append(eval(input("Digite o valor: ")))

res = 0
for i in range(qtd):
    res += lista[i]

print(res/qtd)
