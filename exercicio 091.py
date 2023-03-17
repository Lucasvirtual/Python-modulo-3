from random import randint
from operator import itemgetter
ranking = dict()
jogo = {"jogador1": randint(1,10),
        "jogador2": randint(1,10),
        "jogador3": randint(1,10),
        "jogador4": randint(1,10)
       }

for k, v in jogo.items():
    print("{} tirou {} no dado.".format(k,v))


print("== RANKING DOS JOGADORES ==")
ranking = sorted(jogo.items(), key=itemgetter(1),reverse=True)

print(ranking)