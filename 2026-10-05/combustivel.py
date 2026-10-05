def calcularConsumo(distancia, volume):
  consumo = distancia/volume
  print(f"O consumo médio do veículo foi: {consumo}")

dist = eval(input("Insira a distância: "))
vol = eval(input("Insira o volume: "))

calcularConsumo(dist, vol)