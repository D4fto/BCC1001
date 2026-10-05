def calcularJuros(capInicial, taxa, tempo):
  
  juros = capInicial * taxa/100 * tempo
  montante = capInicial + juros

  return juros


capInicial = eval(input("Insira o capital inicial: "))
taxa = eval(input("Insira a taxa de juros (%): "))
tempo = eval(input("Insira o tempo de aplicação: "))


juros = calcularJuros(capInicial, taxa, tempo)
montante = capInicial + juros

print(f"O Montante é R$ {montante:.2f}")