#Escreva um programa que leia N números inteiros (máximo 20) e armazene em um vetor X. Calcule a média dos elementos do vetor e informe quantos elementos estão abaixo da média do conjunto.
#Crie as seguintes funções:
#• Uma função que faça a leitura dos elementos de um vetor de inteiros. Essa função deve receber como parâmetro o número de elementos do vetor e deve retornar o vetor preenchido.
#• Uma função que calcule a média dos elementos de um vetor. Essa função deve receber como parâmetro um vetor e retornar a média dos elementos dele.
#• Uma função que receba um vetor e um número, e retorne quantos elementos do vetor estão abaixo desse número.

def le_vetor(tamanho):
    v = []
    for i in range(tamanho):
        v.append(int(input('digite um valor para a lista: ')))
    return v

def media_vet(vetor):
    total = 0
    for i in range(len(vetor)):
        total += vetor[i]
    return total/len(vetor)

def abaixo(vetor, num):
    cont = 0
    for i in range(len(vetor)):
        if vetor[i] < num:
            cont += 1
    return cont

    
T = int(input('quantos serão os números? '))
vetor = le_vetor(T)
med = media_vet(vetor)

print(f'números abaixo da média da lista: {abaixo( vetor , med )}')