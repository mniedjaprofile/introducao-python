#TP1 - Exercicio 9
#===== Calcular descontos progressivos ===== 

def calcular_descontos(valor_pedido):
    if valor_pedido > 500:
        desconto = 0.25
    elif valor_pedido > 200: 
        desconto = 0.15
    elif valor_pedido > 100:
        desconto = 0.10
    else:
        desconto = 0.0

    valor_desconto = valor_pedido * desconto
    valor_final = valor_pedido - valor_desconto

    return desconto, valor_final

valor_pedido = float(input("Digite o valor da compra em R$: "))
valor_desconto, valor_final = calcular_descontos(valor_pedido)

print(f"\nValor original da compra: R$ {valor_pedido:.2f}")
print(f"\nDesconto aplicado: R$ {valor_desconto:.2f}")
print(f"\nValor final com desconto: R$ {valor_final:.2f}")