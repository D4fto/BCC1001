def verificaSinal(num):
    if(num>=0):
        print(f"O número {num} é positivo")
    else:
        print(f"O número {num} é negativo")
        
numero = eval(input("Insira um número: "))

verificaSinal(numero)