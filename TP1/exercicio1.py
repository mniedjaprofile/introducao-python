#TP1 - Exercicio 1
#===== Lista de funções para programa principal de calculadora simples ===== 

def entradaDeDados():
    arg1 = float(input("Entre com o primeiro valor: \n"))
    arg2 = float(input("Entre com o segundo valor: \n"))

#calculos
    soma = arg1 + arg2
    sub = arg1 - arg2
    mult = arg1 * arg2
    div = arg1 / arg2 if arg2 != 0 else "Error! Divisão por zero"
    div_int = arg1 // arg2 if arg2 != 0 else "Error! Divisão por zero"

#reusltados
    print(f"Soma: {soma}")
    print(f"Subtração: {sub}")
    print(f"Multiplicação: {mult}")
    print(f"Divisão: {div}")
    print(f"Divisão Inteira: {div_int}")

entradaDeDados()


