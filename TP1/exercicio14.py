# TP1 - Exercicio 14
# ===== Votação ===== 

def votar():
    votos_opcao1 = 0
    votos_opcao2 = 0
    votos_opcao3 = 0

    print("Por favor, escolha uma das opções de candidatos a seguir: ")
    print("1 - Candidato A")
    print("2 - Candidato B")
    print("3 - Candidato C")
    print("0 - Encerrar votação")

    while True:
        voto = int(input("Digite o número correspondente à sua escolha: "))

        if voto == 1:
            votos_opcao1 += 1
            print("Você votou no Candidato A.")

        elif voto == 2:
            votos_opcao2 += 1
            print("Você votou no Candidato B.")
        
        elif voto == 3:
            votos_opcao3 += 1
            print("Você votou no Candidato C.")

        elif voto == 0:
            print("Votação encerrada.")
            break
        else:
            print(" Opção inválida! Escolha de 1 a 3 ou 0 para encerrar.")

    # Exibe os resultados após a votação ser encerrada
    print("\n Resultados da Eleição:")
    print(f"Candidato A: {votos_opcao1} voto(s)")
    print(f"Candidato B: {votos_opcao2} voto(s)")
    print(f"Candidato C: {votos_opcao3} voto(s)")

# Executa 
votar()
