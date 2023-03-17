dados1 = {"nome":"Lucas" , "idade":22,}       
dados2 = {"nome":"Andre" , "idade":21 }
dados3 = {"nome":"Amauricio" , "idade":21}

pessoas = []
dados1["sexo"]="M"
dados2["sexo"]="M"
dados3["sexo"]="M"

pessoas.append(dados1)
pessoas.append(dados2)
pessoas.append(dados3)

print(pessoas[0]["nome"])
print(dados1["nome"])



for k,v in pessoas():
    print("O {} é {}".format(k,v))



#print(dados1["nome"])
#print(dados1["sexo"])
#print(dados1.keys())
#print(dados1.items())
