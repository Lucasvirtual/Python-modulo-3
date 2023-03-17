lista = []
maior = 0
menor = 1000

for c in range(0,5):
    lista.append(int(input("Digite números: ")))

    if lista[c] > maior:
        maior = lista[c]
    if lista[c] < menor:
        menor = lista[c]

for i, v in enumerate(lista):  
    if v == maior:
        print("A posição {} é o {}".format(i,maior))
for i, v in enumerate(lista):
    if v == menor:
        print("A posição {} é o {}".format(i,menor))