#Testando operadores
#Testing operators
n1 = int(input('Digite um valor: '))
n2 = int(input('Outro valor: '))
soma = n1 + n2
multi = n1 * n2
divi = n1 / n2
diviint = n1 // n2
expo = n1 ** n2
print('A soma é {}, o produto é {} e a divisão é {:.3f}'.format(soma,multi,divi), end = ' ')
print('Divisão inteira {} e potência {}'.format(diviint, expo))