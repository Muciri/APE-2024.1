#escreva uma função chamada somar que receba como parâmetro um vetor e retorne a soma dos seus elementos (obs: não use a função sum)
#escreva também um programa que, dado o vetor V = [6,3,8,7,2,5] e usando a função somar criada, imprima a soma dos elementos do vetor V.

def somar(vetor):
    som = 0
    for i in range(len(vetor)):
        som += vetor[i]
    return(som)

V = [6,3,8,7,2,5]
print(f'soma: {somar(V)}')