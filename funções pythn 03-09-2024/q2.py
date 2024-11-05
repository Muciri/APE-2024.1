#Escreva uma função chamada fatorial que receba como parâmetro um número inteiro e retorne seu fatorial. Faça também um programa para testar a função.

def fatorial(n):
    mult = 1
    for n in range(num,0, -1):
        mult *= n
    return mult

num = int(input('digite um número: \n--> '))
resultado = fatorial(num)
print(resultado)