from random import randint
from time import sleep
palpites = []
sorteio = int(input("Quantos jogos você quer que eu sorteie ? "))

for c in range (0, sorteio):
    for j in range(0, 6):
    
        palpites.append(randint(0,60))

print(f"Jogo {c + 1}: {palpites}")
sleep(1)
