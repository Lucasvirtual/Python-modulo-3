lanche = ("Hamburger" , "Suco" , "Pizza" , "Pudim")



for c, lanche1  in enumerate (lanche):
    print(c, lanche1)
print("-" * 50)
for cont in range (0, len(lanche)):
    print(lanche[cont])
print(lanche.index("Pizza"))