dic = {}
listGol = []
nome = str(input("Nome do jogador: "))
partidas = int(input(f"Quantas partidas {nome} jogou ?"))
for c in range(0,partidas):
    gols = int(input(f"Quantos gols na partida {c} ? "))
    listGol.append(gols)
    total = sum(listGol)
    
dic={"nome": nome, "gols" : listGol, "total":total}

print(dic)
print()
print(f"O campo nome tem o valor",dic["nome"])
print(f"O campo gols tem o valor",dic["gols"])
print(f"O campo total tem o valor",dic["total"])
print()
print("O jogador {} jogou {} partidas".format(dic["nome"],partidas))

for i, v in enumerate (dic["gols"]):
    print(f"Na partida {i}, fez {v} gols.")
print("Foi um total de {} gols".format(dic["total"]))


