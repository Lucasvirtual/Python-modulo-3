lista = []
while True:


    numeros = int(input("Digite os valores: "))

    if numeros not in lista:
        lista.append(numeros)
    
    r = str(input("Quer continuar ? [S/N]"))
    if r in "Nn":
        
        break
        
print(lista)