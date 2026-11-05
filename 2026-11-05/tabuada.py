def mostrarTabuada(num):
  i = 1
  print(f"Tabuada do {num}")
  while (i<=10):
    print(f"{num} x {i} = {num * i}")
    i+=1
  print("Acabou a tabuada!")
  
numero = int(input("Insira um número: "))

if(numero >=1 and numero <= 10):
  mostrarTabuada(numero)
else:
  print("O número deve estar entre 1 e 10")