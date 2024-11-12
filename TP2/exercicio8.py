def somar_listas(lista1, lista2):
    """
    Soma os elementos de duas listas de mesma comprimento e retorna uma nova lista com os resultados.
    """
    lista_soma = []
    
    for i in range(len(lista1)):
        soma = lista1[i] + lista2[i]
        lista_soma.append(soma)
    
    return lista_soma

# Definindo as listas
lista1 = [1, 2, 3, 4, 5, 6, 7, 8]
lista2 = [10, 20, 30, 40, 50, 60, 70, 80]


resultado = somar_listas(lista1, lista2)
print("A soma das listas é:", resultado)
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

numeros = ler_numeros()
exibir_invertido(numeros)
