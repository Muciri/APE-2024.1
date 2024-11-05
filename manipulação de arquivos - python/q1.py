name = input('qual o nome do arquivo? ')

arquivo = open(name, 'w+')

arquivole = open(name, 'r')
conteudo = arquivole.read()
print(conteudo)