def calcular_fatorial(n):
    """"
    Calcular  fatorial de um numero inteiro positivo.
    
    Parâmetros
    - n (int): O numero para o qual vamos calcular o fatorial

    Retorna:
    - int: o fatorial de n
    """

    fatorial = 1

    for i in range(1, n + 1):
        fatorial += i
    
    return fatorial

def processamento():
    """"
    Le uma sequencia de numeros inteiros posiivos, 
    calcula e exibe o fatorial de cada numero digitado.
    O programa é encerrado ao ser digitado zero.

    """
    while True:
        numero = int(input("\nDigite um numero inteiro positivo ou 0 (zero) para sair: "))

        if numero == 0:
            print(f"Programa encerrado!!")
            break
        
        elif numero < 0:
            print(f"Numero invalido! Digite apenas numeros inteiros positivos.")
        else:
            print(f"Fatorial de {numero}  é: {calcular_fatorial(numero)}")
    
processamento()