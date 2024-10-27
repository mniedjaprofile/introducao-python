# TP1 - Exercicio 12
# ===== Classificar palavras ===== 

def classificar_palavras():
    curtas = []
    longas = []
    
    print("Digite até 3 palavras para classificá-las como curtas ou longas.")
    print("Você deve inserir pelo menos 2 palavras.")
    print("Digite 'sair' para encerrar o programa.")

    while True: 
        if len(curtas) + len(longas) >= 3: 
            break

        palavra = input("Insira uma palavra: ").strip()
        
        if palavra.lower() == 'sair':
            break

        if len(palavra) < 5:
            curtas.append(palavra)
        else:
            longas.append(palavra)

    total_palavras = len(curtas) + len(longas)
    if total_palavras < 2: 
        print("Você precisa inserir pelo menos 2 palavras para classificar.")
    else:
        print("Palavras Curtas (menos de 5 letras):", ", ".join(curtas) if curtas else "Nenhuma palavra curta.")
        print("Palavras Longas (5 letras ou mais):", ", ".join(longas) if longas else "Nenhuma palavra longa.")

# Executa o programa
classificar_palavras()
