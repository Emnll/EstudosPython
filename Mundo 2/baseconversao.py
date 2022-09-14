num = int(input("Digite um número para conversão: "))
def menu():
    print("----"*5)
    print(" Bases de conversão")
    print("----"*5)
    print("| [1] Binario      |")
    print("| [2] Octal        |")
    print("| [3] Hexadecimal  |")
    print("| [4] Sair         |")
    print("| [5] Ver opções   |")
menu()
lop = True
while lop == True:
    escolha = int(input("Esolha uma opção: "))
    if escolha == 1:
        print("O num {} em binário é {}".format(num,bin(num)[2:]))
    elif escolha == 2:
        print("O num {} em octal é {}".format(num,oct(num)[2:]))
    elif escolha == 3:
        print("O num {} em hexadecimal é {}".format(num,hex(num)[2:]))
    elif escolha == 4:
        print("Volte sempre!")
        lop = False
    elif escolha == 5:
        menu()
    else: 
        print("Por favor digite um número disponível!")
        menu()