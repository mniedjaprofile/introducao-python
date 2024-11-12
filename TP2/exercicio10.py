def ler_numeros():
    """
    Lê uma sequência de números terminada pelo número zero.
    Retorna uma lista contendo os números sem incluir o zero.
    """
    numeros = []
    while True:
        numero = int(input("Digite um número (0 para terminar): "))
        if numero == 0:
            break
        numeros.append(numero)
    return numeros

def exibir_maiores_ou_iguais_a_media(numeros):
    """
    Exibe os números da lista que são maiores ou iguais à média.
    """
    if len(numeros) == 0:
        print("Nenhum número foi digitado.")
        return
    
    media = sum(numeros) / len(numeros)
    print(f"\nMédia dos números: {media}")
    print("Números maiores ou iguais à média:")

    for numero in numeros:
        if numero >= media:
            print(numero, end=" ")

# Programa principal
numeros = ler_numeros()
exibir_maiores_ou_iguais_a_media(numeros)
