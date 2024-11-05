#Escreva um programa que leia as 3 notas de um aluno, determine e exiba a sua média e seu conceito. O programa deve conter as seguintes funções:
#• Uma função que recebe como parâmetros as 3 notas do aluno e retorne a sua média (aritmética).
#• Uma função que receba como parâmetro a média do aluno e retorne o seu conceito, de acordo com a tabela abaixo:


def media (n1, n2, n3):
    return (n1 + n2 + n3)/3
    
def conceito(med):
    if med > 8:
        return('A')
    elif med >= 5 and med <8:
        return('B')
    else:
        return('C')

media1 = int(input('digite sua média 1:'))
media2 = int(input('digite sua média 2:'))
media3 = int(input('digite sua média 3:'))

print(f'média: {media(media1, media2, media3)}, conceito: {conceito(media(media1, media2, media3))}')