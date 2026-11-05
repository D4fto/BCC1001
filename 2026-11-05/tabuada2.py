def mostrarTabuada(num):
  i = 1
  print(f"Tabuada do {num}")
  while (i<=10):
    print(f"{num} x {i} = {num * i}")
    i+=1
  print("Acabou a tabuada!")
  
j = 1

while(j<=10):
  mostrarTabuada(j)
  j+=1