boletim = []
boletimMedia = []

while True:
    nome = str(input("Digite o nome: "))
    nota1 = float(input("Digite a primeira nota do aluno:"))
    nota2 = float(input("Digite a segunda nota do aluno:"))
    media = (nota1 + nota2) / 2
    boletim.append([nome, [nota1,nota2], media])
    
    pergunta = str(input("Você quer continuar ?"))
    
    if pergunta == "nao":
        break

print(boletim)
