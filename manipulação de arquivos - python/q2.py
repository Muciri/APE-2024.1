#Escreva um programa que copie um arquivo texto (cujo nome será lido pelo teclado) para um novo arquivo chamado COPIA.TXT, porém substituindo todos os brancos no arquivo por.

nome_arquivo = input('Qual o nome do arquivo? \n--> ')

with open(nome_arquivo, 'r') as arquivo:
    conteudo = arquivo.read()

conteudo_modificado = conteudo.replace(" ", ".")


with open('COPIA.TXT', 'w') as copia:
    copia.write(conteudo_modificado)

print("Arquivo copiado e modificado com sucesso!")