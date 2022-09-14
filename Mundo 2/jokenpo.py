from random import randint
from time import sleep
itens = ('Pedra','Papel','Tesoura')
life = 0
cplife = 0
tot = cplife + life
print("O jogo acaba quando o jogador conseguir 3 pontos!")
while life < 3:
    sleep(1)
    print("-=-=-=-=-"*5)
    print("O placar está PC: {}, Jogador: {}".format(str(cplife),str(life)))
    computador = randint(0,2)
    print(" Suas opções \n [1] Pedra \n [2] Papel \n [3] Tesoura")
    jogador = (int(input("Escolha: "))-1)
    if jogador > 2:
        print("Número inválido!")
    else: 
        print("JO")
        sleep(1)
        print("KEN")
        sleep(1)
        print('PO!!!!')  
        print("O computador jogou {} e o usuário jogou {}, logo o resultado é: ".format(itens[computador],itens[jogador]))
        if computador == 0:
            if jogador == 0: 
                print("Houve um EMPATE!")
            elif jogador == 1:
                print("O JOGADOR ganhou!")
                life = life + 1
            elif jogador == 2:
                print("O COMPUTADOR ganhou!")
                cplife = cplife + 1
            else:
                print("Número inválido!")

        elif computador == 1:
            if jogador == 0: 
                print("O COMPUTADOR ganhou!")
                cplife = cplife + 1
            elif jogador == 1:
                print("Houve um EMPATE")
            elif jogador == 2:
                print("O JOGADOR ganhou!")
                life = life + 1
            else:
                print("Número inválido!")

        elif computador == 2:
            if jogador == 0: 
                print("O JOGADOR ganhou!")
                life = life + 1
            elif jogador == 1:
                print("O COMPUTADOR ganhou!")
                cplife = cplife + 1
            elif jogador == 2:
                print("Houve um EMPATE!")
            else:
                print("Número inválido!")
    
print("O jogo terminou o placar foi de {} para o computador e {} para você!".format(cplife,life))