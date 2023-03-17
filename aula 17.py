#lista = ["b" , "c" , "d" , "e"]
#numeros = list(range(0,11))
lista = []
numeros = []

#lista.append("f")
#lista.insert(0,"a")
#del lista[0]

#if "a" in lista:
#    lista.remove("a")

for cont in range (0,5):
    lista.append(input("Digite uma letra: "))
    numeros.append(input("Digite uns números: "))

for c, v in enumerate(lista):
    print("{} - {}".format(c,v))
print("------------------------------------------")
for c, v in enumerate(numeros):
    print("{} - {}".format(c,v))

    



#print(lista)
#print(numeros)
#print(len(lista))
#print(len(numeros))


