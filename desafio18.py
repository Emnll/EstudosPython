import math
a = int(input('Digite um ângulo: '))
rad = math.radians(a)
print('O Seno, cosseno e tangente deste ângulo é respectivamente: {:.4f}, {:.4f}, {:.4f}.'.format(math.sin(rad), math.cos(rad),math.tan(rad)))