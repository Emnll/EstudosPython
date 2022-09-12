#Calcula se os números dado pelo usuário podem formar um triângulo
#Calculates if the number given by a user can form a triangle
r1 = float(input('Digite o valor de uma reta: '))
r2 = float(input('Digite o valor de uma reta: '))
r3 = float(input('Digite o valor de uma reta: '))
if (r1+r2>r3) & (r1+r3>r2) & (r2+r3>r1):
    print('Isso pode ser um triângulo!')
else:
    print('Isso não pode formar um triângulo!')