def calcularMedia(nota1, nota2):
    return (nota1 + nota2)/2

nota1 = float(input("Insira a primeira nota: "))
nota2 = float(input("Insira a segunda nota: "))

media = calcularMedia(nota1, nota2)

print(f"A média obtida foi: {media}")

if(media == 10):
    print("Aprovado com distinção")
elif(media>=7):
    print("Aprovado")
else:
    print("Reprovado")