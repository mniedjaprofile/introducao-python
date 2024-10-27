# TP1 - Exercicio 13
# ===== Palíndromo ===== 
# Massa para teste
# Palavras - "arara" , "ana", "ovo", "radar"
# Frases - "Was it a car or a cat I saw?", "socorram me subi no onibus em marrocos"

def palindromo(texto):
    texto = texto.replace(" ", "").lower()
    return texto == texto[::-1] #inverter texto

def core():
    print("Verificador de Palíndromo!")
    frase = input("Digite uma palavra ou frase: ")

    if palindromo(frase):
        print("Caracaaa é um palíndromo!")
    else: 
        print(" '=(' nao e um palíndromo ")

core()