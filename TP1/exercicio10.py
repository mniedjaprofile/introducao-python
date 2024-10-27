#TP1 - Exercicio 10
#===== Historia aleatória ===== 

import random

personagens = [
    "Um jovem guerreiro",
    "Uma sábia anciã",
    "Um ladrão astuto",
    "Uma princesa destemida"
]

acoes = [
    "encontra um mapa antigo",
    "luta contra um dragão feroz",
    "descobre um segredo escondido",
    "salva um aldeão em perigo"
]

locais = [
    "na floresta encantada",
    "em um castelo abandonado",
    "perto de uma montanha sagrada",
    "dentro de uma caverna misteriosa"
]


def criar_historia():
    
    personagem = random.choice(personagens) 
    acao = random.choice(acoes)
    local = random.choice(locais)
    
    historia = f"{personagem} {acao} {local}."
    return historia

print(" Vamos criar uma história! ")
print(criar_historia())
