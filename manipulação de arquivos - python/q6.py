#Escreva um programa que crie um arquivo texto resultante da concatenação de dois outros arquivos.

with open('arquivo1.txt', 'r') as arquivo1:
    conteudo1 = arquivo1.read()

with open('arquivo2.txt', 'r') as arquivo2:
    conteudo2 = arquivo2.read()

with open('arquivo3.txt', 'a') as copia:
    copia.write(f'{conteudo1}')
    copia.write(f'\n{conteudo2}')