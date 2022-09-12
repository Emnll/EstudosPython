#Situação hipotética de um aluguel de carro de locadora que leva em conta os dias alugados e km rodados pelo carro
#Fictional situation where the price of a car rental depends on the total of days that the car will be used and the mileage of the car
d = float(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
total = (60 * d) + (0.15 * km)
print('O total a pagar será de R${:.2f}'.format(total))
