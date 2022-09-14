casa = int(input("Qual o valor da casa: R$"))
salario = int(input("Qual o seu salário: R$ "))
anos = int(input("Em quantos anos você pretende pagar? "))
emprestimo = casa/(12*anos)
print("Para pagar um ama casa de R${:.2f} em {} anos".format(casa,anos))
print(" a prestação será de R${:.2f}".format(emprestimo))
if emprestimo > float(salario)*0.3:
    print("Seu empréstimo foi negado!")
else:
    print("Empréstimo aprovado! A sua casa será paga em {} anos e cada empréstimo será de {} ".format(anos,emprestimo))