#Escreva um programa que leia do teclado o nome de um arquivo texto e uma string, abra o arquivo e inclua no início dele a string lida.

program = input('qual o nome do programa? \n')
string = input('digite uma string \n--> ')

arq = open(program, 'a')
arq.write(string)
arq.close()