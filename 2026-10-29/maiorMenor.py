def maiorMenor(n1, n2, n3):
    maior, menor = 0, 0
    
    if(n1 > n2 and n1 > n3):
        maior = n1
        if(n2 < n3):
            menor = n3
        else:
            menor = n2
    elif(n2 > n3):
        maior = n2
        if(n1 < n3):
            menor = n1
        else:
            menor = n3
    else:
        maior = n3
        if(n1 < n2):
            menor = n1
        else:
            menor = n2
    
    print(f"O maior número é {maior}, o menor é {menor}")

num1 = eval(input("Insira o primeiro número: "))
num2 = eval(input("Insira o segundo número: "))
num3 = eval(input("Insira o terceiro número: "))

maiorMenor(num1, num2, num3)