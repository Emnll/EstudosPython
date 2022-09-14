r1 = float(input('Digite o valor de uma reta: '))
r2 = float(input('Digite o valor de uma reta: '))
r3 = float(input('Digite o valor de uma reta: '))
if (r1+r2>r3) & (r1+r3>r2) & (r2+r3>r1):
    if r1 == r2 == r3:
        print("Será um triângulo equilátero!")
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print("Será um triângulo Isósceles!")
    else:
        print("Será um triângulo escaleno!")
else:
    print('Isso não pode formar um triângulo!')