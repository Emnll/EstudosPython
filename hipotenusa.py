#Calculo da hipotenusa dos números dados
#Calculating the hypot of the given number
from math import hypot
co = int(input('Digite um valor para o cateto oposto: '))
ca = int(input('Digite um valor para o cateto adjacente: '))
print('A hipotenusa desse triângulo tem valor de', hypot(ca,co))