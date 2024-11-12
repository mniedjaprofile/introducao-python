def eh_par(numero):
    """
    Verifica se um número é par.

    Parâmetros:
        numero (int): O número a ser verificado.

    Retorna:
        bool: Retorna True se o número for par, caso contrário, False.
    """
    return numero % 2 == 0

def separar_pares_impares(lista):
    """
    Separa os números de uma lista em duas listas: pares e ímpares.

    Parâmetros:
        lista (list): A lista de números a ser separada.

    Retorna:
        tuple: Uma tupla contendo duas listas, a primeira com números pares e a segunda com números ímpares.
    """
    pares = []
    impares = []

    for numero in lista:
        if eh_par(numero):
            pares.append(numero)
        else:
            impares.append(numero)

    return pares, impares

# Lista de números
numeros = [10, 2, 30, 4, 50, 6, 70, 8, 9, 1]

# Separação de pares e ímpares
pares, impares = separar_pares_impares(numeros)

print("Números pares:", pares)
print("Números ímpares:", impares)
