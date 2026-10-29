def verificaTipoLetra(letra):
    letraOriginal = letra
    letra = letra.lower()
    
    match letra:
        case 'a' | 'e' | 'i' | 'o' | 'u':
            print(f'A letra "{letraOriginal}" é uma vogal!')
        case _:
            print(f'A letra "{letraOriginal}" é uma consoante!')
        
letra = input("Insira uma letra: ")

verificaTipoLetra(letra)