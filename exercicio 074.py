from random import randint
maior = 0
menor = 20
tupla = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))

for c in tupla:
    if c > maior:
        maior = c

    if c < menor:
        menor = c

print("Os números da tupla são", tupla)

print("O maior número da tupla é: ",maior)
print("O menor número da tupla é: ",menor)

