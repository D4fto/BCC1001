def fatiarTempo(totalSegundos):
  resto = totalSegundos % (60 * 60)
  horas = totalSegundos // (60 * 60)
  minutos = resto // 60
  resto %= 60
  segundos = resto

  print(f"{horas}H {minutos}min {segundos}s")


total = eval(input("Insira o total de tempo em segundos: "))

fatiarTempo(total)