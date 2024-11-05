#Faça um programa que leia duas matrizes de inteiros e gere uma terceira matriz que corresponderá a soma das duas matrizes lidas. A ordem das matrizes também será lida. 
#O programa deverá conter as seguintes funções:
#• Uma função para gerar e ler uma matriz, sendo passados como parâmetros a ordem da matriz.
#• Uma função para exibir uma matriz em sua representação clássica (linhas e colunas).
#• Uma função para somar duas matrizes.

def lematriz(linha=3, coluna=3):
    matriz = [ [None]*coluna for i in range(linha) ]
    for l in range(linha):
        for c in range(coluna):
            matriz[l][c] = int(input(f'digite um valor para {l} x {c}'))
            
def imp-matriz(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])
    
    for l in range(linha):
        for c in range(coluna):
            matriz[l][c] = int(input(f'digite um valor para {l} x {c}'))
    
def soma_matriz(mat1, mat2):
    linhas = len(mat1)
    colunas = len(mat1[0])
    mat_soma = [ [None]*coluna for i in range(linha) ]
    
    for l in range(linha):
        for c in range(coluna):
            mat_soma[l][c] = mat1[l][c] + mat2[l][c]            
            
mat_a = lematriz()
mat_b = lematriz()
mat_s = soma_matriz(mat_a, mat_b):
    
print('primeira matriz: \n')
print(mat_a)
print('segunda matriz: \n')
print(mat_b)
print('soma das matrizes: \n')
print(mat_s)