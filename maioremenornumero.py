#Calcula o menor e maior número dados pelo usuário utilizando a técnica de sort
#Calculates the biggest and smallest number given b7 the user using the sort technique
n1 = int(input('Digite um número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
n = [n1,n2,n3].sort()
print('O maior número é: ',n[0])
print('O menor número é: ',n[2])