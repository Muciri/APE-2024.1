#escreva uma função chamada identidade que receba como parâmetro uma matriz quadrada e retorne True se ela for uma matriz identidade, ou False caso contrário
#OBS: matriz identidade é uma matriz quadrada em que os elementos da diagonal principal são iguais a 1 e os demais elementos são iguais a 0. 
#escreva também um programa que leia uma matriz 3x3 de inteiros e diga se ela é ou não é uma matriz identidade (usando a funlção identidade criada).

def identidade(matriz):
    id = True
    for l in range(len(matriz)):
        for c in range(len(matriz)):
            if l != c and matriz[l][c] != 0:
                id = False
            if l == c and matriz[l][c] != 1:
                id = False
    return id

N = 3
matrizz = [[None] *N for i in range(N)]

for l in range(N):
    for c in range(N):
        matrizz[l][c] = int(input(f'digite um elemento para o valor: {l}x{c} '))
        print(f'{identidade(matrizz)}')

mat = identidade(matrizz)
print(mat)