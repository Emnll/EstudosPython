#Calculando o seno, cosseno e tangente de um ângulo dado pelo usuário
#Calculating the sen, cos and tg of a angle given by the user
import math
a = int(input('Digite um ângulo: '))
rad = math.radians(a)
print('O Seno, cosseno e tangente deste ângulo é respectivamente: {:.4f}, {:.4f}, {:.4f}.'.format(math.sin(rad), math.cos(rad),math.tan(rad)))
