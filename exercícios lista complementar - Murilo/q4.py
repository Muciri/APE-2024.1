#escreva um programa para ler 6 números distintos, ou seja, não podem repetir. Exiba os números lidos

V = []*6
c = 0

while True:
    num = int(input('digite um número: '))
    if V.count(num) == 0:
        V.append(num)
        c +=1
    else:
        print('número repetido, tente novalente')
    if c == 6:
        break
print(V)
