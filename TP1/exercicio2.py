#TP1 - Exercicio 2
#===== Conversor de número fornecido de minutos em hrs e minutos e depois faça o inverso. ===== 

def minutos_para_horas(minutos):
    horas = minutos // 60
    minutos_restantes = minutos % 60
    return horas, minutos_restantes

def horas_para_minutos(horas, minutos):
    return horas * 60 + minutos

def main():
    print("Bem-vindo(a) ao meu primeiro conversor!  \n")
    
    # Converter minutos para horas e minutos
    minutos = int(input("Quantos minutos você quer converter para horas e minutos? \n"))
    horas, minutos_restantes = minutos_para_horas(minutos)
    print(f" {minutos} minutos equivalem a {horas} horas e {minutos_restantes} minutos.\n")
    
    # Converter de volta para os minutos totais
    minutos_totais = horas_para_minutos(horas, minutos_restantes)
    print(f" {horas} horas e {minutos_restantes} minutos equivalem a {minutos_totais} minutos no total.\n")


# Executa o programa
main()
