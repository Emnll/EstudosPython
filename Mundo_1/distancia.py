#Calcula a passagem baseado na distância do destino, podendo usar duas tarifas
#Calculates the ticket based on the distance from the destination, being able to use two fares
d = float(input('Qual a distância do destino em Km? '))
if d < 200.00:
    print('O valor da passagem será de:',(d*0.5))
else:
    print('O valor da passagem será de: ',(d*0.45))
