def gerar_pa(primeiro, segundo, quantidade):
    """"
    Gera e exibe uma rogressão Aritmetica (PA) a partir de dois números.

    - Parametros:
        primeiro (init):  O primeiro termo da PA.
        segundo (init): O segundo termo da PA, usado para calcula a razão.
        quantidade (init): O número de termos a serem exibidos...
    """

    razao = segundo - primeiro
    termo_atual = primeiro

    print(f"\nProgressão Aritmetica (PA): ")
    for i in range(quantidade):
        print(f"Termo {i + 1}: {termo_atual}")
        termo_atual += razao

primeiro = int(input("Digite o primeiro termo da PA: "))
segundo = int(input("Digite o segundo termo da PA: "))
quantidade = int(input("Quantos termos você quer na PA? "))

# Executa o programa para gerar a PA
gerar_pa(primeiro, segundo, quantidade)