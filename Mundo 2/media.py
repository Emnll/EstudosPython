n1 = input("Qual o valor da sua primeira prova? ")
n2 = input("Qual o valor da sua segunda prova? ")
m = (float(n1)+float(n2))/2
if float(m) < 5.0:
    print("Você foi reprovado!")
elif float(m) >= 5.0:
    print("Você está de recuperação!")
elif float(m) >= 7.0:
    print("Parabéns, você foi aprovado!")
