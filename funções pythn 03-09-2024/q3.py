#escreva uma função chamada vertical que receba como parâmetro uma strinc e a exiba na vertical, ou seja, com uma letra em cada linha. Faça também um programa para testar a função.

def vertical(string):
    
    print(f'{string} na vertical:')
    for i in range(len(string)):
        print(string[i])

str = input('digite uma string: \n--> ')
vertical(str)