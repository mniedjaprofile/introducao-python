def contar_vogais():
    """
    Lê sequencia de caracteres terminada termiando o programa se o ponto (.) for digitado
    e conta o numero de vogais dgitada até encontrar o ponto.

    Retorna:
    - contagem_vogais (int): o total de vogais digitadas antes do ponto final.
    """

    contagem_vogais = 0
    vogais = "aeiouAEIOU"
    posicao = 1

    while True:
        caracteres = input("Digite uma frase e termine-a com (.): ")

        if caracteres == ".":
            break
        
        print(f"\nEncontre o ponto (.): {caracteres} ")
        posicao += 1 

        if caracteres in vogais:
            contagem_vogais += 1 
    
    return contagem_vogais

print("Número de vogais: ", contar_vogais())