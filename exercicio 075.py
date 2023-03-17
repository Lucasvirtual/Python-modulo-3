tupla = (int(input("Digite o primeiro valor: ")),
         int(input("Digite o segundo valor: ")),
         int(input("Digite o terceiro valor: ")),
         int(input("Digite o quarto valor: ")))

if 3 in tupla:
    print(f"A posição de 3 é {tupla.index(3)}")
print(f"O valor 9 apareceu {tupla.count(9)}x")

for c, tupla1 in enumerate(tupla):
    
    if tupla1 % 2 ==0:
        pares = tupla1
        print(f"Os números pares foram {pares}")