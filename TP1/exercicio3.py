#TP1 - Exercicio 3
#===== Receber dois nomes e combinar de forma criativa ===== 

def combinar_nomes(name1, name2):
    pt1 = name1[:len(name1) // 2]
    pt2 = name2[:len(name2) // 2]
    new_name = pt1 + pt2
    return new_name
    
#Interação com usuário
name1 = input("Digite o primeiro nome:  \n")
name2 = input("Digite o segundo nome:  \n")

#core
new_name = combinar_nomes(name1, name2)
print(f"O novo nome criativo é {new_name}")