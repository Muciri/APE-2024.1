#Escreva um programa para ler 6 números. Após a leitura, verifique para cada um deles, se é distinto, ou seja: não possui repetição

V = [None]*6


for i in range(6):
    V[i] = int(input('digite um número: '))
print(V)

for j in V:
    #print(j)
    if V.count(j) > 1:
        print(f'{j} se repete')
    else:
        print(f'{j} não se repete')