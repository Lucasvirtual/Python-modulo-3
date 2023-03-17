lista = [[],[]]
for c in range(1,8):
    numeros = int(input("Digite o {}º valor: ".format(c)))
    
    
    if numeros % 2 == 0:
        lista[0].append(numeros)
        lista[0].sort()
    
    if numeros % 2 == 1:
        lista[1].append(numeros)
        lista[1].sort()

print("Os números foram: ",lista)
print("Os pares foram: ",lista[0])
print("Os impares foram: ",lista[1])