#Escreva uma função chamada primo para determinar se um número é primo ou não. A função deve receber um número inteiro, retornar True se o número for primo, ou False caso contrário.
#Escreva também um programa que, usando a função primo criada, exiba os números primos entre 1 e 100.


def primo(num):
    resp = True
    if num != 1 and num != 2:
        for i in range(2, num):
            if num%i == 0:
                resp = False
    return(resp)

cont = 0
print('números primos de 0 a 100:')
for i in range(1, 101):
    if primo(i):
        print(i, end = '; ')