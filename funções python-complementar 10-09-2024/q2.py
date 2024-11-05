#Escreva uma função chamada vogal que receba uma letra e verifique se a letra é uma vogal, retornando o valor True nesse caso, ou o valor False caso contrário.
#Escreva também um programa que leia uma frase e, usando a função vogal criada, imprima a quantidade de vogais existentes na frase lida.


def vogal(letra):
    if letra.lower() in 'aeiou':
        return True
        
frase = input('digite uma frase:')
cont = 0

for i in frase:
    if vogal(i):
        cont +=1
        
print(f'a frase tem {cont} vogais')
