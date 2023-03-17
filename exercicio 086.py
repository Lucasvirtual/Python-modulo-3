import numpy as np
matriz = [[0,0,0], [0,0,0], [0,0,0]]
for c in range(0,3):
    for j in range(0,3):
        matriz[c][j] = int(input("Digite um valor para [{}, {}]".format(c,j)))

for c in range(0,3):
        for j in range(0,3):
             print(f"[{matriz[c][j]:^5}]", end="")
        print()     