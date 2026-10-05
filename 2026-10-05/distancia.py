def calcularDistancia(x1, y1, x2, y2):
  distancia = ((x2-x1)**2+(y2-y1)**2)**(1/2)

  print(f"A distância euclidiana entre os pontos é: {distancia}")

x1 = eval(input("Insira a coordena X do primeiro ponto: "))
y1 = eval(input("Insira a coordena Y do primeiro ponto: "))
x2 = eval(input("Insira a coordena X do segundo ponto: "))
y2 = eval(input("Insira a coordena Y do segundo ponto: "))

calcularDistancia(x1, y1, x2, y2)