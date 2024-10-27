#TP1 - Exercicio 7
#===== IMC ===== 

def calcular_imc (peso, altura):
    return peso / (altura ** 2)

print(" Claculadora de IMC ")
peso = float(input("Digite seu peso em kg: \n"))
altura = float(input("Digite sua altura em metros: \n"))

imc = calcular_imc(peso, altura)

print(f"\n Seu IMC é {imc:.2f}")

if imc < 18.5:
    print("Voce esta abaixo do peso.")
elif 18.5 <= imc < 24.9:
    print("Voce esta com peso normal.")
elif 25 <= imc < 29.9:
    print("Voce esta com sobrepeso.")
else:
    print("Voce esta com obesidade.")