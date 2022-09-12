#O programa oferece um menu de funcionalidades e então executa a opção escolhida até que o usuário aperte 3 para sair
print("===="*5)
print("|    M E N U    |")
print("===="*5)
print("| [1] De 1 a 10 |")
print("| [2] De 10 a 1 |")
print("| [3] Sair      |")
print("===="*5)
answer = True
while (answer == True):
    um = 0
    dois = 10

    resp = int(input("Escolha: "))
    if (resp == 1):
     while(um < 10):
        print(str(um) + "...")
        um = um + 1
    elif(resp == 2):
        while(dois > 0):
            print(str(dois) + "...")
            dois = dois - 1
    elif(resp==3):
        print("Tchau tchau!")
        answer = False    
    else:
        print("Escolha outro número!")
    
