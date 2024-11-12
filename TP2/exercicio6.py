def gerar_pa(primeiro, segundo, quantidade):
    """
    Gera uma lista de termos de uma Progressão Aritmética (PA) a partir de dois números.

    Parâmetros:
        primeiro (int): O primeiro termo da PA.
        segundo (int): O segundo termo da PA, usado para calcular a razão.
        quantidade (int): O número de termos a serem gerados.

    Retorna:
        list: Uma lista contendo os termos da PA.
    """

    razao = segundo - primeiro
    termo_atual = primeiro
    pa = []

    for _ in range(quantidade):
        pa.append(termo_atual)
        termo_atual += razao

    return pa
