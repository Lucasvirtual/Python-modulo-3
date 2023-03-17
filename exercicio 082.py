lista = []
listaP = []
listaI = []

for c in range(0,7):
    numeros = int(input("Digite os valores: "))
    lista.append(numeros)
    if numeros % 2 == 0:
        listaP.append(numeros)
    
    if numeros % 2 != 0:
        listaI.append(numeros)

print("Os números digitados foram: ",lista)
print("Os números pares é: ",listaP)
print("Os números impares é: ",listaI)