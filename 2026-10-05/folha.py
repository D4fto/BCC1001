def calcularSalario(qtdHoras, valorHora):
  taxaImposto = 8/100 #8%

  salarioBruto = qtdHoras * valorHora
  salarioLiquido = salarioBruto * (1 - taxaImposto)

  print(f"O salário líquido é: {salarioLiquido:.2f}")

qtd = eval(input("Insira a quantidade de horas trabalhadas: "))
valor = eval(input("Insira o valor pot hora trabalhada: "))

calcularSalario(qtd, valor)