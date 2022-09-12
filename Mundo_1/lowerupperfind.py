#Aqui se usa upper, lower e find para manipular uma string
#Here it is used upper, lower and find to manipulate a string
nome = input('Digite o seu nome completo: ')
print('Seu nome em letras maiúsculas é',nome.upper())
print('Seu nome em letras minúsculas é',nome.lower())
a = len(nome) - nome.count(' ')
print('O total de letras no seu nome é',a)
nn = nome.split()
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
