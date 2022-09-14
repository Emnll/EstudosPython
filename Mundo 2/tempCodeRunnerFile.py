
        print("Marca-texto foi adicionado ao carrinho!")
    elif escolha == 5:
        carrinho.append("Timer Pomodoro")
        pagamento = pagamento + 29.9
        print("Timer pomodoro foi adicionado ao carrinho!")
    elif escolha == 6:
        print("O seu carrinho no momento contém: "+str(carrinho)+" e o total é de "+str(pagamento))
    elif escolha == 7:
        print("Você irá levar: "+ str(carrinho) + " dando um total de "+str(pagamento))
        compra = False
    else:
        print("Número inválido, por favor tente novamente")
print("--------"*5)
print("Formas de pagamento: ")
print("|[1] Dinheiro/Cheque: 10% de desconto  |")
print("|[2]Cartão: 5% de desconto             |\n|[3] 2x no cartão: preço normal        |\n|[4] 3x ou mais no cartão: 20% de juros|")
print("--------"*5)
pag = int(input("Como será a forma de pagamento? "))

if pag == 1:
    fecha = pagamento * 0.9
    print("Você paga {}!".format(fecha))
elif pag == 2:
    fecha = pagamento * 0.95
    print("Você paga {}!".format(fecha))
elif pag == 3:
    fecha = pagamento
    print("Você paga {}!".format(fecha))
elif pag == 4:
    fecha = pagamento * 1.20
    print("Você paga um total de {}!".format(fecha))
