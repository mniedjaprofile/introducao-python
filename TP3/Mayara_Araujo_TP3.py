"""
Este arquivo contém uma coleção de programas simples em Python relacionados
à manipulação de strings, datas e operações básicas.

Programas incluídos:
1. concatenar_nome_e_sobrenome
2. validar_nome_e_sobrenome_com_split
3. exibir_sobrenome_nome
4. data_em_formato_inteiro
5. validar_data
6. data_em_formato_textual
7. verificar_palindromo
8. contagem_vogais
9. formatar_numero_telefone
10. dia_da_semana
11. formatar_cpf
12. inverter_frase_com_slicing
13. inverter_frase_com_slicing
14. cinco_primeiros_e_ultimos_caracteres
15. substituir_ponto_virgula_por_virgula
16. calculo_de_media_com_fstrings
"""

def concatenar_nome_e_sobrenome():
    """
    Solicita um nome e um sobrenome ao usuário,
    concatena-os e exibe o nome completo.
    """
    nome = input("Entre com o nome: ")
    sobrenome = input("Entre com o sobrenome: ")
    nome_completo = f"{nome} {sobrenome}"
    print(nome_completo)


def validar_nome_e_sobrenome_com_split():
    """
    Solicita ao usuário que insira um nome e sobrenome na mesma linha,
    separados por um espaço, e valida a entrada com as seguintes regras:
    - O nome e o sobrenome devem ter pelo menos dois caracteres.
    
    Caso a entrada não seja válida, solicita uma nova entrada.
    Após validar, exibe o nome completo válido.
    """
    while True:
        entrada = input("Digite o nome e o sobrenome separados por um espaço: ")
        partes = entrada.split()
        if len(partes) == 2 and len(partes[0]) >= 2 and len(partes[1]) >= 2:
            print(f"Entrada válida! Nome completo: {entrada}")
            break
        else:
            print("Erro: O nome e o sobrenome devem ter pelo menos dois caracteres e serem separados por um espaço. Tente novamente.")


def exibir_sobrenome_nome():
    """
    Solicita ao usuário um nome e sobrenome na mesma linha e exibe o nome
    no formato "SOBRENOME, Nome".
    """
    entrada = input("Digite o nome e o sobrenome separados por um espaço: ")
    partes = entrada.split()
    if len(partes) == 2:
        nome = partes[0].capitalize()
        sobrenome = partes[1].upper()
        print(f"{sobrenome}, {nome}")
    else:
        print("Erro: Certifique-se de digitar o nome e o sobrenome separados por um espaço.")


def data_em_formato_inteiro():
    """
    Solicita ao usuário uma data no formato "dd/mm/aaaa" e exibe o dia,
    mês e ano como números inteiros.
    """
    data = input("Digite a data no formato dd/mm/aaaa: ")
    partes = data.split("/")
    if len(partes) == 3 and all(parte.isdigit() for parte in partes):
        dia, mes, ano = map(int, partes)
        print(f"Dia: {dia}, Mês: {mes}, Ano: {ano}")
    else:
        print("Erro: Certifique-se de digitar a data no formato correto (dd/mm/aaaa).")


def validar_data():
    """
    Solicita ao usuário uma data no formato "dd/mm/aaaa" e valida a data fornecida.
    - Verifica se o formato da data é válido.
    - Verifica os limites de dia para cada mês, considerando anos bissextos.

    Exemplos:
    - Entrada: "29/02/2024" -> Saída: "Data válida."
    - Entrada: "29/02/2023" -> Saída: "Data inválida."
    """
    while True:
        data = input("Digite a data no formato dd/mm/aaaa (ou 'sair' para encerrar): ").strip()

        if data.lower() == "sair":
            print("Encerrando a validação de data.")
            break

        partes = data.split("/")
        if len(partes) == 3 and all(parte.isdigit() for parte in partes):
            dia, mes, ano = map(int, partes)
            
            if not (1 <= mes <= 12):
                print("Data inválida: mês fora do intervalo permitido (1-12).")
                continue

            dias_por_mes = {
                1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
                7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
            }

            if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
                dias_por_mes[2] = 29

            if 1 <= dia <= dias_por_mes[mes]:
                print("Data válida.")
            else:
                print("Data inválida: dia fora do intervalo permitido para o mês.")
        else:
            print("Formato inválido. Certifique-se de digitar a data no formato dd/mm/aaaa.")


def data_em_formato_textual():
    """
    Solicita uma data no formato 'dd/mm/aaaa' e exibe a data formatada como 
    'dia de nome_do_mês de ano'.
    
    - Exemplo de entrada: '02/11/2024'
    - Exemplo de saída: '02 de novembro de 2024'
    """
    meses = {
        1: "janeiro", 2: "fevereiro", 3: "março", 4: "abril", 5: "maio", 6: "junho",
        7: "julho", 8: "agosto", 9: "setembro", 10: "outubro", 11: "novembro", 12: "dezembro"
    }
    
    while True:
        data = input("Digite a data no formato dd/mm/aaaa (ou 'sair' para encerrar): ").strip()

        if data.lower() == "sair":
            print("Encerrando a formatação de data textual.")
            break
        
        partes = data.split("/")
        if len(partes) == 3 and all(parte.isdigit() for parte in partes):
            dia, mes, ano = map(int, partes)
            if 1 <= mes <= 12 and 1 <= dia <= 31:
                nome_do_mes = meses.get(mes, None)
                if nome_do_mes:
                    print(f"{dia:02d} de {nome_do_mes} de {ano}")
                else:
                    print("Data inválida: mês fora do intervalo permitido.")
            else:
                print("Data inválida: dia ou mês fora do intervalo permitido.")
        else:
            print("Formato inválido. Certifique-se de digitar a data no formato dd/mm/aaaa.")

def contar_vogais():
    """
    Solicita uma frase ao usuário e conta o número de vogais (a, e, i, o, u) presentes na frase.
    Exemplo: Para a entrada "Ana Paula", o programa deverá exibir "5 vogais".
    """
    frase = input("Digite uma frase: ").strip()
    contador_vogais = 0
    vogais = "aeiouAEIOU"  # Considerando vogais minúsculas e maiúsculas

    for char in frase:
        if char in vogais:
            contador_vogais += 1

    print(f"A frase '{frase}' tem {contador_vogais} vogais.")


def verificar_palindromo():
    """
    Verifica se uma palavra fornecida pelo usuário é um palíndromo.

    - Um palíndromo é uma palavra que pode ser lida de forma idêntica da esquerda para a direita e vice-versa.
    - Exemplo de palavras: 'ovo', 'osso', 'anilina'.

    Saída:
    - Mensagem informando se a palavra é ou não um palíndromo.
    """
    while True:
        palavra = input("Digite uma palavra para verificar se é um palíndromo (ou 'sair' para encerrar): ").strip()

        if palavra.lower() == "sair":
            print("Encerrando a verificação de palíndromos.")
            break

        if not palavra.isalpha():
            print("Entrada inválida. Digite apenas letras.")
            continue

        inverso = palavra[::-1]  # Inverte a palavra
        if palavra.lower() == inverso.lower():
            print(f"'{palavra}' é um palíndromo!")
        else:
            print(f"'{palavra}' não é um palíndromo.")


def contagem_vogais():
    """
    Conta o número de vogais em uma frase fornecida pelo usuário.
    """
    frase = input("Digite uma frase: ").strip()
    vogais = "aeiouAEIOU"
    contador_vogais = sum(1 for char in frase if char in vogais)
    
    print(f"A frase '{frase}' tem {contador_vogais} vogais.")


def formatar_numero_telefone():
    """
    Solicita um número de telefone e exibe no formato (99) 99999-9999, validando a entrada.
    """
    while True:
        telefone = input("Digite um número de telefone (11 dígitos): ").strip()
        
        if len(telefone) != 11 or not telefone.isdigit():
            print("Erro: o número deve conter exatamente 11 dígitos.")
            continue
        
        # Formata o número de telefone
        formatted_telefone = f"({telefone[:2]}) {telefone[2:7]}-{telefone[7:]}"
        print(f"Número formatado: {formatted_telefone}")
        break


def dia_da_semana():
    """
    Solicita um número entre 1 e 7 e exibe o dia da semana correspondente.
    """
    dias_da_semana = {
        1: "Segunda-feira", 2: "Terça-feira", 3: "Quarta-feira",
        4: "Quinta-feira", 5: "Sexta-feira", 6: "Sábado", 7: "Domingo"
    }
    
    while True:
        try:
            dia = int(input("Digite um número de 1 a 7 para representar um dia da semana: "))
            if 1 <= dia <= 7:
                print(f"O dia da semana é: {dias_da_semana[dia]}")
                break
            else:
                print("Erro: Digite um número entre 1 e 7.")
        except ValueError:
            print("Erro: Digite um número válido.")


def formatar_cpf():
    """
    Solicita um CPF (apenas números) e exibe no formato 'xxx.xxx.xxx-xx'.
    """
    while True:
        cpf = input("Digite o CPF (apenas números): ").strip()
        
        if len(cpf) == 11 and cpf.isdigit():
            formatted_cpf = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
            print(f"CPF formatado: {formatted_cpf}")
            break
        else:
            print("Erro: O CPF deve conter exatamente 11 números.")

def inverter_frase():
    """
    Inverte uma frase fornecida pelo usuário usando um loop `for`.

    Solicita uma frase ao usuário, constrói sua versão invertida caractere a caractere
    utilizando um loop, e exibe o resultado.
    
    Args:
    Nenhum.

    Returns:
    Nenhum. A função imprime o resultado diretamente.
    """
    frase = input("Digite uma frase: ").strip()

    # Inverte a frase usando 'for'
    frase_invertida = ''.join([frase[i] for i in range(len(frase) - 1, -1, -1)])

    print(f"Frase invertida: {frase_invertida}")

def inverter_frase_com_slicing():
    """
    Inverte a frase digitada pelo usuário usando slicing.
    """
    frase = input("Digite uma frase: ")
    frase_invertida = frase[::-1]
    print(f"Frase invertida: {frase_invertida}")


def cinco_primeiros_e_ultimos_caracteres():
    """
    Exibe os cinco primeiros e os cinco últimos caracteres de uma frase.
    """
    frase = input("Digite uma frase: ")
    primeiros = frase[:5]
    ultimos = frase[-5:]
    print(f"Cinco primeiros caracteres: {primeiros}")
    print(f"Cinco últimos caracteres: {ultimos}")


def substituir_ponto_virgula_por_virgula():
    """
    Substitui todos os pontos e vírgulas de uma frase por vírgulas.
    """
    frase = input("Digite uma frase com pontos e vírgulas: ")
    nova_frase = frase.replace(";", ",")
    print(f"Nova frase: {nova_frase}")


def calculo_de_media_com_fstrings():
    """
    Calcula a média de três números fornecidos pelo usuário, exibindo a resposta com f-strings.
    """
    while True:
        try:
            numero1 = float(input("Digite o primeiro número: "))
            numero2 = float(input("Digite o segundo número: "))
            numero3 = float(input("Digite o terceiro número: "))
            media = (numero1 + numero2 + numero3) / 3
            print(f"A média dos três números é: {media:.2f}")
            break
        except ValueError:
            print("Erro: Digite apenas números válidos.")


if __name__ == "__main__":
    while True:
        print("\nEscolha o programa a executar:")
        print("1. Concatenar Nome e Sobrenome")
        print("2. Validar Nome e Sobrenome com Split")
        print("3. Exibir Sobrenome, Nome")
        print("4. Data em Formato Inteiro")
        print("5. Validar Data")
        print("6. Data em Formato Textual")
        print("7. Verificar Palíndromo")
        print("8. Contar Vogais")
        print("9. Formatar Número de Telefone")
        print("10. Dia da Semana")
        print("11. Formatar CPF")
        print("12. Inverter Frase com For")
        print("13. Inverter Frase com Slicing")
        print("14. Cinco Primeiros e Últimos Caracteres")
        print("15. Substituir ';' por ','")
        print("16. Cálculo de Média com f-strings")
        print("17. Sair")
        
        escolha = input("Digite o número do programa que deseja executar: ").strip()
        
        if escolha == "1":
            concatenar_nome_e_sobrenome()
        elif escolha == "2":
            validar_nome_e_sobrenome_com_split()
        elif escolha == "3":
            exibir_sobrenome_nome()
        elif escolha == "4":
            data_em_formato_inteiro()
        elif escolha == "5":
            validar_data()
        elif escolha == "6":
            data_em_formato_textual()
        elif escolha == "7":
            verificar_palindromo()
        elif escolha == "8":
            contar_vogais()
        elif escolha == "9":
            formatar_numero_telefone()
        elif escolha == "10":
            dia_da_semana()
        elif escolha == "11":
            formatar_cpf()
        elif escolha == "12":
            inverter_frase()
        elif escolha == "13":
             inverter_frase_com_slicing()
        elif escolha == "14":
            cinco_primeiros_e_ultimos_caracteres()
        elif escolha == "15":
            substituir_ponto_virgula_por_virgula()
        elif escolha == "16":
            calculo_de_media_com_fstrings()
        elif escolha == "17":
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")
