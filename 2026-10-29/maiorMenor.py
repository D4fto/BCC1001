def maiorMenor(n1, n2, n3):
    
    if(n1 > n2 and n1 > n3):
        if(n2 < n3):
            print(n1, n2)
        else:
            print(n1, n3)
    elif(n2 > n3):
        if(n1 < n3):
            print(n2, n1)
        else:
            print(n2, n3)
    else:
        if(n1 < n2):
            print(n3, n1)
        else:
            print(n3, n2)
    

num1 = eval(input("Insira o primeiro número: "))
num2 = eval(input("Insira o segundo número: "))
num3 = eval(input("Insira o terceiro número: "))

maiorMenor(num1, num2, num3)