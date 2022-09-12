#Using if and else to calculate the reaction
#Usando operadores de lógica para clcular a reação da máquina
n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
m = (n1 + n2)/2
print('A sua média foi: ',m)
if m >= 7.0:
    print('Sua média foi boa! PARABÉNS')
else:
    print('Sua média foi ruim! Boa sorte na próxima!')