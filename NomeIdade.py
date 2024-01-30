import datetime

def obter_ano_nascimento():
    while True:
        try:
            ano_nascimento = int(input("Digite o ano de nascimento (entre 1922 e 2024): "))
            if 1922 <= ano_nascimento <= 2024:
                return ano_nascimento
            else:
                print("Erro: O ano de nascimento deve estar entre 1922 e 2024.")
        except ValueError:
            print("Erro: Insira um valor numérico válido.")

def calcular_idade(ano_nascimento):
    ano_atual = datetime.datetime.now().year
    idade = ano_atual - ano_nascimento
    return idade


nome_completo = input("Digite seu nome completo: ")

ano_nascimento = obter_ano_nascimento()

idade = calcular_idade(ano_nascimento)

print(f"\nNome: {nome_completo}")
print(f"Idade: {idade} anos (em 2024)")
