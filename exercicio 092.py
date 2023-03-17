from datetime import datetime
dados = {}

dados["nome"] = str(input("Nome: "))
dados["nascimento"] = int(input("Ano de nascimento: "))
dados["carteira"] = int(input("Carteira de trabalho (0 não tem) "))
dados["idade"] = datetime.now().year - dados["nascimento"]

if dados["carteira"] == 0:
    print(dados)
    
if dados["carteira"] >= 1:
    dados["contratacao"] = int(input("Ano de contratação "))
    dados["salario"] = float(input("Salário: R$"))
    dados["aposentadoria"] = dados["idade"] + ((dados["contratacao"] + 35) - datetime.now().year)
    print(dados)