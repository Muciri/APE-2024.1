#dados dois vetores A e B contendo N elementos inteiros cada (N, A e B serão lidos), gerar e exibir um vetor C (de tamanho N*2) cujos elementos sejam a intercalação dos 
#elementos de A e B
#Ex: N = 3, A = [18,12,20], B = [15,10,7], C = [18,15,12,10,20,7]

N = int(input('quantos serão os números? '))
A = []*N
B = []*N
C = []*N*2

for i in range(N):
    num = int(input('adicione um número a A: '))
    A.append(num)

for j in range(N):
    num = int(input('adicione um número a B: '))
    B.append(num)

for K in A:
    C.append(K)

for L in B:
    C.append(L)

print(A)
print(B)
print(C)
