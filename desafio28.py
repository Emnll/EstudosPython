import random
n = random.randint(0,5)
guess = int(input('Escolha um número de 0 - 5: '))
if guess == n:
    print('Você acertou!')
else:
    print('Você errou!')