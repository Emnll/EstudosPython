#Conta a quantidade de A, encontra a posição do primeiro a pela direita e pela esquerda
#Count the quantity of As, finds the position of the first a by the right and by the left
n1 = input('Digite seu nome completo: ').upper().strip()
print(n1.count('A'))
print(n1.find('A')+1)
print(n1.rfind('A')+1)
