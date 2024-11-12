def calcular_estatisticas(lista):
    """
    Calcula e exibe o menor valor, o maior valor, a soma e a média dos elementos de uma lista.
    
    Parâmetros:
        lista (list): A lista de números a ser analisada.
    """
    menor = lista[0]
    maior = lista[0]
    soma = 0
    
    for numero in lista:
        if numero < menor:
            menor = numero
        if numero > maior:
            maior = numero
        soma += numero
    
    media = soma / len(lista)

    print(f"Menor valor: {menor}")
    print(f"Maior valor: {maior}")
    print(f"Soma dos elementos: {soma}")
    print(f"Média dos elementos: {media}")

# Lista de números
numeros = [10, 2, 30, 4, 50, 6, 70, 8, 9, 1]
calcular_estatisticas(numeros)
