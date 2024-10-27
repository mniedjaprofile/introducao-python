# TP1 - Exercicio 16
# ===== Impar ou par ===== 

def verificar_impar_ou_par():
    print("Vamos descobrir se o numero que voce digitar é impar ou par!! ")

    while True:
        try:
            numero = int(input("Por favor digite um numero inteiro: "))
            break 
        except ValueError:
            print("Isso não é um numero valido. Tente novamente.")

    if numero % 2 == 0:
        resultado = "par"
    else:
        resultado = "Ímpar"

    print(f"O numero {numero} é {resultado}.")

#executar
verificar_impar_ou_par()

