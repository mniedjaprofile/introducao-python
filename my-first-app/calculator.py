#Refatorando código de aula
#===== Lista de funções para programa principal de calculadora simples ===== 

def menu():
    print("\n ---- Menu Calculator ----\n")
    print("[1] - Somar")
    print("[2] - Subtrair")
    print("[3] - Multiplicar")
    print("[4] - Dividir")
    operador = int(input("Entre com o tipo de operação desejada: \n"))
    return operador

def entradaDeDados():
    arg1 = float(input("Entre com o primeiro valor: \n"))
    arg2 = float(input("Entre com o segundo valor: \n"))
    return arg1, arg2

def soma(arg1, arg2):
    result = (arg1 + arg2)
    print("Operação escolhida foi SOMA \n Resultado: ",result)

def subtrair(arg1, arg2):
    result = (arg1 - arg2)
    print("Operação escolhida foi SUBTRAÇÃO \n Resultado: ",result)

def multiplicar(arg1, arg2):
    result = (arg1 * arg2)
    print("Operação escolhida foi MULTIPLICAÇÃO \n Resultado: ",result)

def dividir(arg1, arg2):
    if arg2 != 0:
        result = (arg1 / arg2)
        print("Operação escolhida foi DIVISÃO \n Resultado: " ,result)
    else:
        print("Erro! Não é possivel dividir por Zero")        

# CORE App
def calcular():
    oper = menu()
    value = entradaDeDados()
#
    match oper:
        case 1:
            soma(*value)
        case 2:
            subtrair(*value)
        case 3:
            multiplicar(*value)
        case 4:
            dividir(*value)

calcular()


