N = int(input('quantos números serão lidos? '))
V = [None]*N
cont_P = 0
cont_I = 0
soma = 0


for i in range(N):
    V[i] = int(input('digite um número: '))
    soma += V[i]
    if (V[i] %2 ==0):
        cont_P +=1
    else:
        cont_I +=1


print(f'lista: {V}')
print(f'quantidade de elementos pares: {cont_P}')
print(f'quantidade de elementos ímpares: {cont_I}')
print(f'soma dos elementos: {soma}')
print(f'média dos elementos {soma/N}')