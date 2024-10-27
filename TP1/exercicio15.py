# TP1 - Exercicio 15
# ===== Aventura Interativa  ===== 

def aventura():
    print("Você é um programador renomado em uma empresa de tecnologia.")
    print("Hoje, um bug crítico apareceu em um de seus aplicativos, e você precisa tomar decisões rápidas para resolver a situação.")
    print("Você está prestes a apresentar seu trabalho em uma reunião importante.")

    escolha1 = input("Você: \n1 - Fica até tarde corrigindo o bug. \n2 - Apresenta a versão atual e tenta resolver depois. \nEscolha (1 ou 2): ")

    match escolha1:
        case '1':
            print("\n Você decide ficar até tarde. Após horas de trabalho, você encontra a solução!")
            print("Na reunião, sua equipe fica impressionada com sua dedicação.")
            print("Você é promovido a líder de projeto e ganha um bônus!")
        case '2':
            print("\n Você decide apresentar a versão atual. Durante a apresentação, o bug aparece!")
            print("Os investidores ficam preocupados e sua equipe deve trabalhar em uma correção de emergência.")
            print("Você aprende a importância de testes antes de apresentações.")
        case _:
            print("\n Opção inválida! A reunião começa sem você.")
        
    print("\n Fim da aventura. Pense bem nas suas escolhas na próxima vez!")

# Executar
aventura()
