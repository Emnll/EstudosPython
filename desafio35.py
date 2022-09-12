r1 = float(input('Digite o valor de uma reta: '))
r2 = float(input('Digite o valor de uma reta: '))
r3 = float(input('Digite o valor de uma reta: '))
if (r1+r2>r3) & (r1+r3>r2) & (r2+r3>r1):
    print('Isso pode ser um triângulo!')
else:
    print('Isso não pode formar um triângulo!')