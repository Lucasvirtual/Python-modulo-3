import numpy as np
matriz = [[0,0,0], [0,0,0], [0,0,0]]
matrizpares = []
matrizterceira = []
maior = 0
matrizSegunda = []
scol = 0
for c in range(0,3):
    for j in range(0,3):
        matriz[c][j] = int(input("Digite um valor para [{}, {}] ".format(c,j)))

        if matriz[c][j] % 2 == 0:
            matrizpares.append(matriz[c][j])
            soma = sum(matrizpares)
        
for j in range(0 , 3):
    scol += matriz[j][2]
print("A soma dos valores da terceira coluna é  ",scol)

for c in range (0, 3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
         maior = matriz[1][c]   
print("O maior número da segunda linha é: ",maior)

print("A soma dos números pares é: ",soma) 