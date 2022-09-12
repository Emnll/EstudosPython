#Usando split encontra seu primeiro nome e último sobrenome
#Using the split it finds your first name and last surname
nome = input('Digite seu nome completo: ')
n1 = nome.split()
print('O seu primeiro nome é {} e seu ultimo sobrenome é {}'.format(n1[0],n1[-1]))
