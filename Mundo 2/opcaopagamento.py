from time import sleep


compra = True
pagamento = 0.0
carrinho = []

print("-------"*5)
print("            Poppy Mall  ")
print("-------"*5)
print("Produtos: ")
print("|[1] Post-it: R$ 5.0             |")
print("|[2] Caneta Muji: R$ 10.0        |\n|[3] Caderno Inteligente: R$ 40.5|\n|[4] Marca-texto: R$ 10.5        |\n|[5] Timer pomodoro: R$ 29.9     |\n|[6] Ver carrinho                |\n|[7] Fechar compra               |")
while compra == True:
    sleep(1)
    print("-------"*5)
    escolha = int(input("Qual(is) produtos gostaria de levar hoje? "))
    if escolha == 1:
        carrinho.append("Post-it")
        pagamento = pagamento + 5.0
        print("Post-it foi adicionado ao carrinho!")
    elif escolha == 2:
        carrinho.append("Caneta Muji")
        pagamento = pagamento + 10.0
        print("Caneta muji foi adicionado ao carrinho!")
    elif escolha == 3:
        carrinho.append("Caderno Inteligente")
        pagamento = pagamento + 40.5
        print("Caderno Inteligente foi adicionado ao carrinho")
    elif escolha == 4:
        carrinho.append("Marca Texto")
        pagamento = pagamento + 10.5
        print("Marca-texto foi adicionado ao carrinho!")
    elif escolha == 5:
        carrinho.append("Timer Pomodoro")
        pagamento = pagamento + 29.9
        print("Timer pomodoro foi adicionado ao carrinho!")
    elif escolha == 6:
        print("O seu carrinho no momento contém: "+str(carrinho)+" e o total é de "+str(pagamento))
    elif escolha == 7:
        print("Você irá levar: "+ str(carrinho) + " dando um total de R$"+str(pagamento))
        compra = False
    else:
        print("Número inválido, por favor tente novamente")
print("--------"*5)
print("Formas de pagamento: ")
print("|[1] Dinheiro/Cheque: 10% de desconto  |")
print("|[2] Cartão: 5% de desconto            |\n|[3] 2x no cartão: preço normal        |\n|[4] 3x ou mais no cartão: 20% de juros|")
print("--------"*5)
pag = int(input("Como será a forma de pagamento? "))

if pag == 1:
    fecha = pagamento * 0.9
    print("Você paga R${}!".format(fecha))
elif pag == 2:
    fecha = pagamento * 0.95
    print("Você paga R${}!".format(fecha))
elif pag == 3:
    fecha = pagamento
    print("Você paga R${}!".format(fecha))
elif pag == 4:
    fecha = pagamento * 1.20
    print("Você paga um total de R${}!".format(fecha))
