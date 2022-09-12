#Da ao usuário a unidade, dezena, centena e milhar de um número
#Gives the user the house of unity, ten, hundred and thousando of a given number

num = int(input('Digite um Número de 0 - 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Unidade',u)
print('Dezena',d)
print('Centena',c)
print('Milhar',m)