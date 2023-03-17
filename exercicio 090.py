boletimDic = {}

boletimDic["nome"] = str(input("Digite o nome do aluno: "))
boletimDic["media"] = float(input("Digite a media do aluno: "))

if boletimDic["media"] > 7:
    boletimDic["situacao"] = "Aprovado"

if boletimDic["media"] < 7:
    boletimDic["situacao"] = "Reprovado"

print("O nome dele é {} e a media é {}".format(boletimDic["nome"],boletimDic["media"]))
print("E ele está",boletimDic["situacao"])