lista = []
cont = 0

while True:
    
    numero = int(input("Digite os valores: "))
    cont += 1
    lista.append(numero)
    lista.sort(reverse=True)
        
      
    
    r = str(input("Você quer continuar ? [S/N]"))    
    if r in "Nn":
        break

if 5 in lista:
    print("O número 5 está na lista")   
else:
    print("o número 5 não está na lista") 

print("Foram digitados {} números".format(cont))
print(lista) 