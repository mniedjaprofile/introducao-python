#TP1 - Exercicio 11
#===== Girar dados ===== 

import random

def girar_dados(qtd_dados):
    resultados = []
    for i in range(qtd_dados):
        resultado = random.randint(1, 6) #Possibilidades de resultado
        resultados.append(resultado)
    return resultados

def mostrar_resultados(resultados):
    print("\n Resultados dos Lançamentos ")
    for i, resultado in enumerate(resultados):
        if resultado == 1:
            print(f"Dado {i+1}:  Um! Você perdeu a sorte!")
        elif resultado == 6:
            print(f"Dado {i+1}:  Seis! Jackpot! Você é o rei dos dados!")
        else:
            print(f"Dado {i+1}: {resultado}")

def main():
    print("Gire os dados e vamos ver se vc esta com sorte hoje! ")
    
    while True:
        try:
            qtd_dados = int(input("Quantos dados você quer lançar? (1 a 10): "))
            if 1 <= qtd_dados <= 10:
                break
            else:
                print("Por favor, escolha um número entre 1 e 10.")
        except ValueError:
            print("Entrada inválida! Digite um número inteiro.")
    
    resultados = girar_dados(qtd_dados)
    mostrar_resultados(resultados)

# Executa o programa
main()
