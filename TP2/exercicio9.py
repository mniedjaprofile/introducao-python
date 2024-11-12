def ler_numeros():
    """
    Lê uma sequência de números terminada pelo número zero.
    Retorna a lista de números sem incluir o zero.
    """
    numeros = []
    while True:
        numero = int(input("Digite um número (0 para terminar): "))
        if numero == 0:
            break
        numeros.append(numero)
    return numeros

def exibir_invertido(numeros):
    """
    Exibe a lista de números na ordem invertida.
    """
    print("Números na ordem invertida:")
    for i in range(len(numeros) - 1, -1, -1):
        print(numeros[i], end=" ")

# Programa principal
numeros = ler_numeros()
exibir_invertido(numeros)
