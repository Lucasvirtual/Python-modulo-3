dic = {}
lista = []
cont = 0
while True:
    
    nome = (str(input("Digite o nome: ")))
    sexo = str(input("Digite o sexo: [M/F] "))            
    idade = int(input("Digite a idade: "))
    cont += 1
    dic = {"nome": nome , "sexo": sexo , "idade": idade}
    lista.append(dic)
    
            
      
    
    pergunta = str(input("Quer continuar ? [S/N]"))   
    if pergunta in "nN":
        break


    

soma = sum(pessoa['idade'] for pessoa in lista)
media = soma / cont

print(f"Ao todo temos {cont} pessoas cadastradas.")
print(f"A média de idade é de {media:.2f} anos.")

#print(f"As mulheres cadastradas foram {p["nome"]}")
#for p in lista:
   # if p["sexo"] == "F":
        #print(f"{p["nome"]}")
for p in lista:
    if p["idade"] >= media:
        for k, v in p.items():
            print(f"{k} = {v}")
