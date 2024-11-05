#Escreva um programa que leia do teclado o nome de um arquivo texto e uma string, abra o arquivo e inclua no final dele a string lida.

program = input('qual o nome do programa? \n-->')
string = input('\ndigite uma string \n--> ')


arq = open(program, 'r+')
arq.write(string)
arq.close()