def mostrarOrdemCrescente(n1, n2, n3):
    primeiro, segundo, terceiro = 0, 0, 0
    
    if(n1 > n2 and n1 > n3):
        primeiro = n1
        if(n2 > n3):
            segundo = n2
            terceiro = n3
        else:
            segundo = n3
            terceiro = n2
    elif(n2 > n3):
        primeiro = n2
        if(n1 > n3):
            segundo = n1
            terceiro = n3
        else:
            segundo = n3
            terceiro = n1
    else:
        primeiro = n3
        if(n1 > n2):
            segundo = n1
            terceiro = n2
        else:
            segundo = n2
            terceiro = n1
    print(f"{primeiro}, {segundo}, {terceiro}")


num1 = eval(input("Insira o primeiro número: "))
num2 = eval(input("Insira o segundo número: "))
num3 = eval(input("Insira o terceiro número: "))

mostrarOrdemCrescente(num1, num2, num3)