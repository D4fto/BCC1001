def defineMaior():
    num1 = eval(input("Insira o primeiro número: "))
    num2 = eval(input("Insira o segundo número: "))
    
    if(num1 > num2):
        return num1
    return num2


maior = defineMaior()

print(f"O maior número é {maior}")
