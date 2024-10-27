#TP1 - Exercicio 6
#===== Advinha ===== 

secret_number = 189

print("Bem-vindo ao jogo de adivinhação! \n")
print("Tente adivinhar o número secreto entre 1 e 200. ")


#core
while True: 
    palpite = int(input("Digite seu palpite:  \n"))
    if palpite == secret_number:
        print("Parabéns! Você acertou o número secreto!")
        break
    
    diferenca = abs(secret_number - palpite)
    
    if 1 <= diferenca <= 10:
        print(" Quase lá! Você está muito próximo!")

    elif palpite < secret_number:
        print("Muito baixo! Tente um número maior.")
   
    else: 
        palpite > secret_number
        print(" Muito alto! Tente um número menor.")

   