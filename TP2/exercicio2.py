def calcular_soma_e_media():
    """"
    Calcula a soma e a media dos numeros de 1 a 100.

    Retorna:
    - soama(int): A soma dos numeros de 1 a 100
    - media (float) A média dos numeros de 1 a 100
    """

    soma = sum(range(1,101))
    media = soma / 100

    return soma, media

soma, media = calcular_soma_e_media()
print(f"Soma dos numeros de 1 a 100: ", soma)
print(f"Média dos numeros de 1 a 100: ", media)