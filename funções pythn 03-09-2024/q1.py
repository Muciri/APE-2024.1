#escreva uma função chamada menor que receba como parâmetro 3 números e retorne o menor deles. Faça também um programa para testar a função.

def menor(n1, n2, n3):
    if n1 <= n2 and n1 <= n3:
        return n1
    if n2 <= n1 and n2 <= n3:
        return n1
    if n3 <= n1 and n3 <= n2:
        return n1
    print(f'o menor número é: {men}')

num1 = int(input('digite um número: \n-->'))
num2 = int(input('digite um número: \n-->'))
num3 = int(input('digite um número: \n-->'))
print(f'menor: {menor(num1,num2,num3)}')

