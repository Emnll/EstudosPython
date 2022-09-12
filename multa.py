#Um pequeno programa que se baseando na velocidade de carro te da uma multa ou não
#Based on the number given by the user it gives you a ticket
v = int(input('Qual a velocidade do carro: '))
if v > 80:
    print('Você foi multado!')
    print('Você terá que pagar R$',((v - 80)*7))

else:
    print('Você não foi multado')
