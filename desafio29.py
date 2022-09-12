v = int(input('Qual a velocidade do carro: '))
if v > 80:
    print('Você foi multado!')
    print('Você terá que pagar R$',((v - 80)*7))

else:
    print('Você não foi multado')
